import abc

from pydantic import BaseModel
from qa.common.models import Reference


class SpeciesImage(BaseModel):
    static_path: str
    short_description: str
    references: list[Reference] | None = None


class AbstractClassification(abc.ABC):
    @abc.abstractmethod
    def topics(self) -> list[str]:
        pass


class LinnaeanTaxonomy(BaseModel, AbstractClassification):
    domain: str | None = None
    kingdom: str | None = None
    phylum: str | None = None
    class_: str | None = None
    order: str | None = None
    family: str | None = None
    tribe: str | None = None
    genus: str | None = None
    species: str | None = None

    def topics(self) -> list[str]:
        classification_topics = []
        dict_model = self.model_dump()
        for field_name, field_value in dict_model.items():
            if field_value is not None:
                classification_topics.append(f"{field_name}:{field_value}")
        return classification_topics


class GeneticClassification(BaseModel, AbstractClassification):
    clades: list[tuple[str, str]]

    def topics(self) -> list[str]:
        for clade in self.clades:
            yield f"{clade[0]}:{clade[1]}"


Classification = LinnaeanTaxonomy | GeneticClassification


class OneSpecies(BaseModel):
    french_name: str
    latin_name: str
    description: str = ""
    images: list[SpeciesImage] | None = None
    classification: Classification | None = None
    references: list[Reference] | None = None


class AllSpecies(BaseModel):
    species: dict[str, OneSpecies]  # Key should be the latin name of the species

