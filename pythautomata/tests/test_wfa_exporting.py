from unittest import TestCase

from pythautomata.automata_definitions.weighted_tomitas_grammars import WeightedTomitasGrammars
from pythautomata.model_exporters.image_exporters.wfa_pdf_image_exporter import WFAImageExporter
from pythautomata.model_exporters.image_exporters.wfa_pdf_image_exporter_with_partition_mapper import WFAImageExporterWithPartitionMapper
from pythautomata.utilities.probability_partitioner import TopKProbabilityPartitioner
from pythautomata.model_exporters.partition_mapper import TopKPartitionMapper


class TestWFAExporting(TestCase):
    def test_1(self):
        wfa = WeightedTomitasGrammars.get_automaton_7()
        WFAImageExporter().export(wfa, "./output_models/tests")
        WFAImageExporterWithPartitionMapper(TopKProbabilityPartitioner(
            1), TopKPartitionMapper()).export(wfa, "./output_models/tests", wfa.name+"partitioned_top_1")
