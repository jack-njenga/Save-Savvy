"""
scraping data part
- description
- prices
- tags
- ratings if posible
- links
"""
from bs4 import BeautifulSoup as bs

class Scrape:
    """Scrape class"""
    soup = ""
    content = ""
    articles = []

    def __init__(self, *args, **kwargs):
        """Initialization"""
        if args and not (self.content):
            for arg in args:
                if isinstance(arg, bytes):
#                     print(type(arg))
                    self.content = arg
                    break
        if kwargs:
            for key, val in kwargs.items():
                if key == "content":
#                     print(f"{key} = {type(val)}")
                    self.content = val
                    break
        if not self.content:
            print("---E-X-(ERROR): Content resource is not available")
            print("--A--(ABORT): Aborting...")
#             return

        if not self.soup:
            try:
                self.soup = bs(self.content, "html.parser")
            except Exception as e:
                print(f"--A--(ALERT): bs4 is not parsing\nFixing... :{e}")
                try:
                    self.soup = bs(self.content)
                except Exception as e:
                    print(f"--E-X-(ERR): bs4 Failed to soup\n\t:{e}")

    def get_data(self, article):
        """
        returns the data
        """
        data = {}
        if article:
            try:
                a_tag = article.find("a", class_="core")
                for key, val in {"link": "href", "description": "text", "category": "data-category"}.items():
                    try:
                        if key == "description":
                            data["description"] = a_tag.text
                        else:
                            data[key] = a_tag[val]
                    except Exception as e:
                        # print(f"--A--(ALERT): Failed to find {e} Value from the a tag ")
                        # print(article)
                        pass
            except Exception as e:
                print(f"--A--(ALERT): Could Not find any 'a' Tag\nTrying to fix...: {e}")
                try:
                    a_tag = article.find_all("a")[0]
                    data.update({"link": a_tag['href'], "description": a_tag.text, "type": a_tag['data-category'].split(" ")[0]})
                    # updates should not fail if present
                except Exception as e:
                    # print(f"--A--(ALERT): Could Not find any 'a' Tag\n\t:{e} not found in {a_tag}\n{article}")
                    pass

            try:
                img = a_tag.find("div", class_="img-c")
                data["image"] = img.find("img")["data-src"]
            except Exception as e:
                print("--A--(ALERT): Img not Found!", e)
                pass

            try:
                info = a_tag.find("div", class_="info")
            except Exception as e:
                print(f"--A--(Alert): Could not find any 'div' Tags\n\t:{e}")
                try:
                    info = a_tag.find_all("div")[-1]
                except Exception as e:
                    print(f"--A--(Alert): Could not find any 'div' Tags\n\t:{e}")

            try:
                name = info.find("h3", class_="name").text.split(",")[0]
                price = info.find("div", class_="prc")
                data.update({"name": name, "price": price.text})
                # updates should not fail if present
            except Exception as e:
                print(f"--A--(Alert): Could not find any 'h3/div' Tags\n\t:{e}")
                try:
                    name = info.find_all("h3")[0].text.split(",")[0]
                    price = info.find_all("div")[0]
                    data.update({"name": name, "price": price.text})
                    # updates should not fail if present
                except Exception as e:
                    print(f"--A--(Alert): Could not find any 'h3/div' Tags\n\t:{e}")
        return data


    def get_articles(self):
        """
        returns a list of all articles
        """
        section = ""
        try:
            section = self.soup.find("section", class_="card")
        except Exception as e:
            print(f"--A--(ALERT) no section with class='card'\nTrying to fix...: {e}")
            try:
                sections = self.soup.find_all("section")
                if len(sections) == 4:
                    section = sections[2]
                else:
                    print(f"--A--(ALERT): All section are {len(sections)} Expected 4 only")
            except Exception as e:
                print("--E--(ERR): Could Not find the Section with class='card' Found...")
                sections = self.soup.find_all("section")
                i = 1
                for sect in sections:
                    print(f"Section {i}: {sect['class']}")
                    i += 1
        if section:
            self.articles = list(section.find_all("article", class_="prd"))
            print(f"\t {len(self.articles)} articles Found")
        else:
            print("--E--(ERR): No section Found Returning 0 articles")
            self.articles = []
            print(f"\t {len(self.articles)} articles Found")
        return self.articles


