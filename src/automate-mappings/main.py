from oaklib import OntologyResource
from schema_automator import SchemaAnnotator
from linkml_runtime import SchemaView

from oaklib.implementations.ontoportal.bioportal_implementation import BioPortalImplementation
from oaklib.resource import OntologyResource
import biolink
from linkml_runtime.dumpers import yaml_dumper
from oaklib.utilities.apikey_manager import set_apikey_value
import os


def main():
    set_apikey_value("bioportal", os.environ["BIOPORTAL_API_KEY"])
    impl = BioPortalImplementation()
    annotator = SchemaAnnotator(impl, curie_only=True, mine_descriptions=True)
    sv = SchemaView(biolink.BIOLINK_MODEL_YAML)
    for eclass in sv.all_classes():
        if "association" not in sv.class_ancestors(eclass):
            print(yaml_dumper.dumps(sv.get_element(eclass)))
            annotator.annotate_element(sv.get_element(eclass))
            print("result...")
            print(yaml_dumper.dumps(sv.get_element(eclass)))

    for enum in sv.all_enums():
        print("enum", enum)
    # annotator.annotate_schema(sv)


if __name__ == '__main__':
    main()
