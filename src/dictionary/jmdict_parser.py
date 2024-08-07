import xml.etree.ElementTree as ET
import os


class JMDictParser:
    def __init__(self):
        self.tree = ET.parse(os.path.join(os.path.dirname(__file__), 'JMdict_e.xml'))
        self.root = self.tree.getroot()
        self.entries = self._get_entries()

    def _get_entries(self):
        """
         Compiles all the entries in JMdict into a list which contains
         the kanji, reading and translational equivalent (gloss)
         grouped as a dict.
        """
        entries = []
        for entry in self.root.findall('entry'):
            kanji_elements = entry.findall('k_ele/keb')
            reading_elements = entry.findall('r_ele/reb')
            sense_elements = entry.findall('sense/gloss')

            kanji = [ke.text for ke in kanji_elements]
            readings = [re.text for re in reading_elements]
            glosses = [gl.text for gl in sense_elements]

            entries.append({
                'kanji': kanji,
                'readings': readings,
                'glosses': glosses
            })
        return entries

    def lookup(self, term):
        """
        Returns the dictionary entry matching the term

        Args:
            term (str): Term to lookup

        Returns:
            A dict containing term reading/kanji/translation or None
        """
        for entry in self.entries:
            if term in entry['kanji'] or term in entry['readings']:
                return entry
        return None


def test_lookup():
    """
    Function to test the JMDictParser Class.
    """
    parser = JMDictParser()
    test_terms = ["こんにちは", "世界", "ありがとう"]  
    for term in test_terms:
        result = parser.lookup(term)
        if result:
            print(f"Lookup result for '{term}':")
            print(f"Kanji: {result.get('kanji', 'N/A')}")
            print(f"Readings: {result.get('readings', 'N/A')}")
            print(f"Glosses: {result.get('glosses', 'N/A')}")
            print("---")
        else:
            print(f"No entry found for '{term}'")
            print("---")


if __name__ == "__main__":
    test_lookup()
