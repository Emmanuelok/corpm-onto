from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDF

from corruptpm.loader import load_example_graph, load_ontology_graph, load_ontology_module_paths
from tests.conftest import ROOT


BASE = "https://w3id.org/corruptpm/"


def test_master_ontology_loads_successfully() -> None:
    graph = load_ontology_graph(root=ROOT)
    assert len(graph) > 0


def test_all_ontology_modules_load_successfully() -> None:
    for module_path in load_ontology_module_paths(root=ROOT):
        graph = Graph()
        graph.parse(module_path.as_posix(), format="turtle")
        assert len(graph) > 0, module_path.name


def test_example_data_loads_successfully() -> None:
    graph = load_example_graph(root=ROOT)
    assert len(graph) > 0


def test_required_top_level_classes_exist() -> None:
    graph = load_ontology_graph(root=ROOT)
    required_classes = [
        "CorruptionEvent",
        "CorruptAct",
        "Project",
        "ProjectPhase",
        "ContractStage",
        "ProjectActor",
        "ActorRole",
        "Cause",
        "Vulnerability",
        "RiskFactor",
        "RedFlag",
        "Impact",
        "AntiCorruptionControl",
        "ControlObjective",
        "Barrier",
        "Indicator",
        "Evidence",
        "CaseStudy",
        "Jurisdiction",
        "GovernanceInstrument",
        "Sanction",
        "DetectionMechanism",
        "ReportingMechanism",
        "ProcurementMethod",
        "AssetOrResource",
        "DecisionPoint",
        "ProjectManagementProcess",
    ]
    for class_name in required_classes:
        uri = URIRef(f"{BASE}{class_name}")
        assert (uri, RDF.type, OWL.Class) in graph, class_name


def test_required_object_properties_exist() -> None:
    graph = load_ontology_graph(root=ROOT)
    required_properties = [
        "involvesActor",
        "hasActorRole",
        "occursInProject",
        "occursInPhase",
        "occursInContractStage",
        "hasCorruptAct",
        "hasCause",
        "hasVulnerability",
        "hasRiskFactor",
        "hasRedFlag",
        "hasImpact",
        "isMitigatedBy",
        "isDetectedBy",
        "isPreventedBy",
        "isEnabledBy",
        "isConstrainedBy",
        "hasBarrier",
        "hasEvidence",
        "hasIndicator",
        "hasControlObjective",
        "governedBy",
        "resultsInSanction",
        "targetsAssetOrResource",
        "exploitsDecisionPoint",
        "affectsStakeholder",
        "relatedToProcurementMethod",
        "documentedInCaseStudy",
        "hasReportingMechanism",
    ]
    for property_name in required_properties:
        uri = URIRef(f"{BASE}{property_name}")
        assert (uri, RDF.type, OWL.ObjectProperty) in graph, property_name


def test_required_data_properties_exist() -> None:
    graph = load_ontology_graph(root=ROOT)
    required_properties = [
        "riskScore",
        "likelihoodScore",
        "impactScore",
        "confidenceScore",
        "monetaryValue",
        "eventDate",
        "detectionDate",
        "description",
        "sourceReference",
        "jurisdictionName",
        "projectValue",
        "projectStartDate",
        "projectEndDate",
        "caseName",
    ]
    for property_name in required_properties:
        uri = URIRef(f"{BASE}{property_name}")
        assert (uri, RDF.type, OWL.DatatypeProperty) in graph, property_name

