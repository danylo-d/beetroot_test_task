import fitz


class Parser:
    def __init__(self, blocks):
        self.blocks = blocks
        self.results = []

    def parse(self):
        for block in self.blocks:
            (
                title,
                session,
                abstract,
                authors,
                affiliations,
                result,
            ) = self.initialize_variables()

            for line in block["lines"]:
                for span in line["spans"]:
                    session_pattern = (
                        span["size"] == 9.5
                        and span["font"] == "TimesNewRomanPS-BoldItal"
                    )
                    title_pattern = (
                        span["size"] == 9 and span["font"] == "TimesNewRomanPS-BoldMT"
                    )
                    aut_aff_pattern = span["font"] == "TimesNewRomanPS-ItalicMT"
                    abstract_pattern = span["size"] == 9.134002685546875

                    text_pattern = span["text"]

                    # get session title
                    if session_pattern:
                        session += text_pattern
                    # get title
                    elif title_pattern:
                        title += text_pattern
                    elif aut_aff_pattern:
                        # get authors list
                        if span["size"] == 9:
                            authors.append(text_pattern)
                        # get affiliations list
                        elif span["size"] == 8:
                            affiliations.append(text_pattern)
                    # get abstract content
                    elif abstract_pattern:
                        abstract += text_pattern

            self._update_result(result, authors, affiliations, session, title, abstract)

    def _update_result(self, result, authors, affiliations, session, title, abstract):
        for author in authors:
            author = author.replace(",", "").strip()
            result[author] = {
                "affiliation": None,
                "person_location": None,
                "session": session,
                "topic_title": title,
                "presentation_abstract": None,
            }

        if result:
            self.results.append([result])

        if affiliations:
            for res in self.results[-1]:
                for key in list(res.keys()):
                    if len(affiliations) == 2:
                        res[key]["affiliation"] = affiliations[0]
                        res[key]["person_location"] = (
                            affiliations[1].replace(",", "").strip()
                        )
                    else:
                        res[key]["affiliation"] = "".join(affiliations)

        if abstract:
            for res in self.results[-1]:
                for key in list(res.keys()):
                    if res[key]["presentation_abstract"] is None:
                        res[key]["presentation_abstract"] = abstract
                    res[key]["presentation_abstract"] += abstract

    def get_parsed_results(self):
        clean_results = []
        for sublist in self.results:
            clean_results.extend(sublist)
        return clean_results

    @staticmethod
    def initialize_variables():
        title = ""
        session = ""
        abstract = ""
        authors = []
        affiliations = []
        result = {}
        return title, session, abstract, authors, affiliations, result


def extract_blocks(doc, start_page):
    blocks = []
    for page_num in range(start_page, len(doc)):
        page = doc.load_page(page_num)
        blocks.extend(page.get_text("dict")["blocks"])
    return blocks


def parse_blocks(pdf_path, start_page):
    with fitz.open(pdf_path) as doc:
        blocks = extract_blocks(doc, start_page)
        parser = Parser(blocks)
        parser.parse()
        return parser.get_parsed_results()
