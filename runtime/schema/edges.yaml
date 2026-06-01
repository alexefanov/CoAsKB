# edges.yaml — Relation contract for graph edges (incl. citations).
#
# Each edge type declares:
#   endpoints   { from: <kind>, to: <kind> }  -- '*' means any kind
#   direction   directed | symmetric           -- symmetric edges are stored once
#                                                 with sorted endpoints
#   workflow    which subsystem owns this edge type
#               (ingest | edit | check | evidence | experiment | provenance | citation | idea)
#   attributes  schema for edge-record fields beyond from/to/type
#
# Storage location of each edge type is decided in conventions.yaml::edge_storage.

# =============================================================================
# INGEST EDGES — Document loading and semantic parsing
# =============================================================================

# ---------------------------------------------------------------------------
# Paper ↔ Paper edges (ingest)
# ---------------------------------------------------------------------------

cites:
  endpoints: { from: papers, to: papers }
  direction: directed
  workflow:  citation
  attributes:
    source: { type: enum, values: [semantic_scholar, parsed_bib, manual], required: true }
    date:   { type: date }

references:
  endpoints: { from: papers, to: papers }
  direction: directed
  workflow:  ingest
  attributes:
    section:  { type: str }
    context:  { type: str }

replaces:
  endpoints: { from: papers, to: papers }
  direction: directed
  workflow:  ingest
  attributes:
    replace_type: { type: enum, values: [full, partial], required: true }
    date:         { type: date }

cancels:
  endpoints: { from: papers, to: papers }
  direction: directed
  workflow:  ingest
  attributes:
    date:    { type: date }
    reason:  { type: str }

amends:
  endpoints: { from: papers, to: papers }
  direction: directed
  workflow:  ingest
  attributes:
    section:    { type: str }
    description: { type: str }

same_problem_as:
  endpoints: { from: papers, to: papers }
  direction: symmetric
  workflow:  ingest
  attributes:
    confidence: { type: enum, values: [high, medium, low], required: true }
    evidence:   { type: str, required: true }

similar_method_to:
  endpoints: { from: papers, to: papers }
  direction: symmetric
  workflow:  ingest
  attributes:
    confidence: { type: enum, values: [high, medium, low], required: true }
    evidence:   { type: str, required: true }

builds_on:
  endpoints: { from: papers, to: papers }
  direction: directed
  workflow:  ingest
  attributes:
    confidence: { type: enum, values: [high, medium, low], required: true }
    evidence:   { type: str, required: true }

challenges:
  endpoints: { from: papers, to: papers }
  direction: directed
  workflow:  ingest
  attributes:
    confidence: { type: enum, values: [high, medium, low], required: true }
    evidence:   { type: str, required: true }

# ---------------------------------------------------------------------------
# Paper → Concept edges (ingest)
# ---------------------------------------------------------------------------

introduces_concept:
  endpoints: { from: papers, to: concepts }
  direction: directed
  workflow:  ingest
  attributes:
    confidence: { type: enum, values: [high, medium, low], required: true }
    evidence:   { type: str, required: true }

uses_concept:
  endpoints: { from: papers, to: concepts }
  direction: directed
  workflow:  ingest
  attributes:
    confidence: { type: enum, values: [high, medium, low], required: true }
    evidence:   { type: str, required: true }

extends_concept:
  endpoints: { from: papers, to: concepts }
  direction: directed
  workflow:  ingest
  attributes:
    confidence: { type: enum, values: [high, medium, low], required: true }
    evidence:   { type: str, required: true }

critiques_concept:
  endpoints: { from: papers, to: concepts }
  direction: directed
  workflow:  ingest
  attributes:
    confidence: { type: enum, values: [high, medium, low], required: true }
    evidence:   { type: str, required: true }

# ---------------------------------------------------------------------------
# Paper → Method edges (ingest)
# ---------------------------------------------------------------------------

regulates:
  endpoints: { from: papers, to: methods }
  direction: directed
  workflow:  ingest
  attributes:
    confidence: { type: enum, values: [high, medium, low], required: true }
    section:    { type: str }

# ---------------------------------------------------------------------------
# Generic ingest edges
# ---------------------------------------------------------------------------

related_to:
  endpoints: { from: '*', to: '*' }
  direction: symmetric
  workflow:  ingest
  attributes:
    note: { type: str }

# =============================================================================
# EDIT EDGES — Wiki structuring and organization
# =============================================================================

contains_subprocess:
  endpoints: { from: methods, to: methods }
  direction: directed
  workflow:  edit
  attributes:
    order:       { type: int }
    description: { type: str }

applies_to:
  endpoints: { from: methods, to: topics }
  direction: directed
  workflow:  edit
  attributes: {}

# =============================================================================
# CHECK EDGES — Integrity verification
# =============================================================================

contradicts:
  endpoints: { from: '*', to: '*' }
  direction: symmetric
  workflow:  check
  attributes:
    severity: { type: enum, values: [explicit, implicit], required: true }
    resolution: { type: str }

# =============================================================================
# EVIDENCE EDGES — Experimental validation
# =============================================================================

supports:
  endpoints: { from: '*', to: '*' }
  direction: directed
  workflow:  evidence
  attributes:
    evidence: { type: str }

confirms:
  endpoints: { from: [methods, experiments], to: concepts }
  direction: directed
  workflow:  evidence
  attributes:
    source: { type: str }

# =============================================================================
# EXPERIMENT EDGES — Research workflow
# =============================================================================

tested_by:
  endpoints: { from: ideas, to: experiments }
  direction: directed
  workflow:  experiment
  attributes:
    evidence: { type: str }

tested_with:
  endpoints: { from: experiments, to: ideas }
  direction: directed
  workflow:  experiment
  attributes:
    evidence: { type: str }

invalidates:
  endpoints: { from: '*', to: '*' }
  direction: directed
  workflow:  experiment
  attributes:
    evidence: { type: str }

verified_by:
  endpoints: { from: methods, to: methods }
  direction: directed
  workflow:  experiment
  attributes: {}

# =============================================================================
# IDEA EDGES — Knowledge gaps and inspiration
# =============================================================================

addresses_gap:
  endpoints: { from: ideas, to: '*' }
  direction: directed
  workflow:  idea
  attributes:
    evidence: { type: str }

inspired_by:
  endpoints: { from: ideas, to: '*' }
  direction: directed
  workflow:  idea
  attributes:
    evidence: { type: str }

# =============================================================================
# PROVENANCE EDGES — Origin tracking
# =============================================================================

derived_from:
  endpoints: { from: '*', to: '*' }
  direction: directed
  workflow:  provenance
  attributes:
    evidence: { type: str }

originated_from:
  endpoints: { from: '*', to: '*' }
  direction: directed
  workflow:  provenance
  attributes: {}
