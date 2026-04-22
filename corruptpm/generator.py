from __future__ import annotations

from pathlib import Path

import yaml

from corruptpm.config import load_config


def generate_construct_ttl(spec: dict[str, object], root: Path | None = None) -> str:
    config = load_config(root)
    base = config.namespace.base_iri
    construct_id = str(spec["id"])
    construct_type = str(spec["type"])
    label = str(spec["label"])
    definition = str(spec["definition"])
    broader = str(spec.get("broader") or construct_type)
    scope_note = spec.get("scope_note")
    related_phases = [str(item) for item in spec.get("related_phases", [])]
    related_stages = [str(item) for item in spec.get("related_contract_stages", [])]
    red_flags = [str(item) for item in spec.get("red_flags", [])]
    controls = [str(item) for item in spec.get("controls", [])]
    subclass_entries = [f"cpm:{broader}"]
    subclass_entries.extend(
        f"[ a owl:Restriction ; owl:onProperty cpm:occursInPhase ; owl:someValuesFrom cpm:{phase} ]"
        for phase in related_phases
    )
    subclass_entries.extend(
        f"[ a owl:Restriction ; owl:onProperty cpm:occursInContractStage ; owl:someValuesFrom cpm:{stage} ]"
        for stage in related_stages
    )
    subclass_entries.extend(
        f"[ a owl:Restriction ; owl:onProperty cpm:hasRedFlag ; owl:someValuesFrom cpm:{red_flag} ]"
        for red_flag in red_flags
    )
    subclass_entries.extend(
        f"[ a owl:Restriction ; owl:onProperty cpm:isMitigatedBy ; owl:someValuesFrom cpm:{control} ]"
        for control in controls
    )

    lines = [
        f"@prefix cpm: <{base}> .",
        "@prefix owl: <http://www.w3.org/2002/07/owl#> .",
        "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .",
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
        "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
        "",
        f"cpm:{construct_id} a owl:Class ;",
        "    rdfs:subClassOf",
    ]
    for index, entry in enumerate(subclass_entries):
        suffix = " ," if index < len(subclass_entries) - 1 else " ;"
        lines.append(f"        {entry}{suffix}")
    lines.append(f'    rdfs:label "{label}"@en ;')
    lines.append(f'    skos:definition "{definition}"@en ;')
    if scope_note:
        lines.append(f'    skos:scopeNote "{scope_note}"@en ;')
    lines.append(f'    skos:inScheme <{base}scheme/constructs> .')
    lines.append("")
    return "\n".join(lines)


def generate_construct_from_yaml(
    input_path: Path,
    *,
    output_path: Path | None = None,
    root: Path | None = None,
) -> tuple[Path | None, str]:
    spec = yaml.safe_load(input_path.read_text(encoding="utf-8"))
    ttl = generate_construct_ttl(spec, root=root)
    if output_path:
        output_path.write_text(ttl, encoding="utf-8")
    return output_path, ttl
