# Ontology Map

```mermaid
graph TD
  CorruptionEvent["CorruptionEvent"]
  CorruptAct["CorruptAct"]
  AbuseOfAuthority["Abuse of authority"] --> CorruptAct
  AbuseOfDiscretion["Abuse of discretion"] --> CorruptAct
  AssetMisappropriation["Asset misappropriation"] --> CorruptAct
  Bribery["Bribery"] --> CorruptAct
  Collusion["Collusion"] --> CorruptAct
  ConfidentialInformationLeakage["Confidential information leakage"] --> CorruptAct
  ConflictOfInterest["Conflict of interest"] --> CorruptAct
  Embezzlement["Embezzlement"] --> CorruptAct
  Project["Project"]
  ProjectPhase["ProjectPhase"]
  CloseoutPhase["Closeout phase"] --> ProjectPhase
  ConstructionOrImplementationPhase["Construction or implementation phase"] --> ProjectPhase
  DesignPhase["Design phase"] --> ProjectPhase
  FeasibilityAndPreInvestmentPhase["Feasibility and pre-investment phase"] --> ProjectPhase
  FinancingAndBudgetAllocationPhase["Financing and budget allocation phase"] --> ProjectPhase
  HandoverAndCommissioningPhase["Handover and commissioning phase"] --> ProjectPhase
  InspectionPhase["Inspection phase"] --> ProjectPhase
  LandAcquisitionAndCompensationPhase["Land acquisition and compensation phase"] --> ProjectPhase
  ContractStage["ContractStage"]
  BidEvaluationStage["Bid evaluation stage"] --> ContractStage
  BidSubmissionStage["Bid submission stage"] --> ContractStage
  ClaimsAndDisputesStage["Claims and disputes stage"] --> ContractStage
  ContractAwardStage["Contract award stage"] --> ContractStage
  ContractClosureStage["Contract closure stage"] --> ContractStage
  ContractExecutionStage["Contract execution stage"] --> ContractStage
  ContractMonitoringStage["Contract monitoring stage"] --> ContractStage
  ContractNegotiationStage["Contract negotiation stage"] --> ContractStage
  ProjectActor["ProjectActor"]
  AntiCorruptionAgency["Anti-corruption agency"] --> ProjectActor
  Auditor["Auditor"] --> ProjectActor
  Client["Client"] --> ProjectActor
  CommunityStakeholder["Community stakeholder"] --> ProjectActor
  Consultant["Consultant"] --> ProjectActor
  ContractManager["Contract manager"] --> ProjectActor
  Contractor["Contractor"] --> ProjectActor
  CourtOrTribunal["Court or tribunal"] --> ProjectActor
  ActorRole["ActorRole"]
  AdvisoryRole["Advisory role"] --> ActorRole
  CommunityOversightRole["Community oversight role"] --> ActorRole
  DecisionAuthorityRole["Decision authority role"] --> ActorRole
  DeliveryRole["Delivery role"] --> ActorRole
  EnforcementRole["Enforcement role"] --> ActorRole
  FinancialControlRole["Financial control role"] --> ActorRole
  OversightRole["Oversight role"] --> ActorRole
  PoliticalRole["Political role"] --> ActorRole
  Cause["Cause"]
  BudgetPressure["Budget pressure"] --> Cause
  CulturalNormalization["Cultural normalization"] --> Cause
  LackOfTransparency["Lack of transparency"] --> Cause
  PoliticalPatronage["Political patronage"] --> Cause
  TimePressure["Time pressure"] --> Cause
  WeakAccountability["Weak accountability"] --> Cause
  WeakGovernance["Weak governance"] --> Cause
  WeakSanctions["Weak sanctions"] --> Cause
  Vulnerability["Vulnerability"]
  ComplexSupplyChain["Complex supply chain"] --> Vulnerability
  DiscretionaryDecisionMaking["Discretionary decision making"] --> Vulnerability
  EmergencyProcurement["Emergency procurement"] --> Vulnerability
  FragmentedProjectDelivery["Fragmented project delivery"] --> Vulnerability
  InadequateCompetition["Inadequate competition"] --> Vulnerability
  InadequateDigitalTraceability["Inadequate digital traceability"] --> Vulnerability
  InformationAsymmetry["Information asymmetry"] --> Vulnerability
  LowDetectionProbability["Low detection probability"] --> Vulnerability
  RiskFactor["RiskFactor"]
  Cause["Cause"] --> RiskFactor
  Vulnerability["Vulnerability"] --> RiskFactor
  RedFlag["RedFlag"]
  AbnormalPaymentPattern["Abnormal payment pattern"] --> RedFlag
  BidPricesTooClose["Bid prices too close"] --> RedFlag
  DelayedInspectionReports["Delayed inspection reports"] --> RedFlag
  ExcessiveUseOfEmergencyProcurement["Excessive use of emergency procurement"] --> RedFlag
  FrequentVariationOrders["Frequent variation orders"] --> RedFlag
  FrontLoadedPayments["Front-loaded payments"] --> RedFlag
  IdenticalBidDocuments["Identical bid documents"] --> RedFlag
  InflatedUnitPrices["Inflated unit prices"] --> RedFlag
  Impact["Impact"]
  CostOverrun["Cost overrun"] --> Impact
  EconomicInefficiency["Economic inefficiency"] --> Impact
  EnvironmentalDamage["Environmental damage"] --> Impact
  InfrastructureUnderperformance["Infrastructure underperformance"] --> Impact
  LegalLiability["Legal liability"] --> Impact
  LossOfValueForMoney["Loss of value for money"] --> Impact
  PoorQuality["Poor quality"] --> Impact
  ProjectFailure["Project failure"] --> Impact
  AntiCorruptionControl["AntiCorruptionControl"]
  AuditControl["Audit control"] --> AntiCorruptionControl
  CommunityOversightControl["Community oversight control"] --> AntiCorruptionControl
  ContractualControl["Contractual control"] --> AntiCorruptionControl
  CorrectiveControl["Corrective control"] --> AntiCorruptionControl
  DetectiveControl["Detective control"] --> AntiCorruptionControl
  DigitalControl["Digital control"] --> AntiCorruptionControl
  FinancialControl["Financial control"] --> AntiCorruptionControl
  GovernanceControl["Governance control"] --> AntiCorruptionControl
  ControlObjective["ControlObjective"]
  AccountabilityObjective["Accountability objective"] --> ControlObjective
  CompetitionObjective["Competition objective"] --> ControlObjective
  DetectionObjective["Detection objective"] --> ControlObjective
  ParticipationObjective["Participation objective"] --> ControlObjective
  PreventionObjective["Prevention objective"] --> ControlObjective
  QualityAssuranceObjective["Quality assurance objective"] --> ControlObjective
  TraceabilityObjective["Traceability objective"] --> ControlObjective
  TransparencyObjective["Transparency objective"] --> ControlObjective
  Barrier["Barrier"]
  CulturalAcceptanceOfCorruption["Cultural acceptance of corruption"] --> Barrier
  DataAvailabilityProblem["Data availability problem"] --> Barrier
  FearOfRetaliation["Fear of retaliation"] --> Barrier
  InstitutionalWeakness["Institutional weakness"] --> Barrier
  LackOfEnforcement["Lack of enforcement"] --> Barrier
  LackOfFunding["Lack of funding"] --> Barrier
  LackOfWhistleblowerProtection["Lack of whistleblower protection"] --> Barrier
  LimitedTechnicalCapacity["Limited technical capacity"] --> Barrier
  Indicator["Indicator"]
  BidConcentrationIndicator["Bid concentration indicator"] --> Indicator
  ChangeOrderRateIndicator["Change order rate indicator"] --> Indicator
  DocumentationCompletenessIndicator["Documentation completeness indicator"] --> Indicator
  InspectionLagIndicator["Inspection lag indicator"] --> Indicator
  PaymentAnomalyIndicator["Payment anomaly indicator"] --> Indicator
  RedFlag["Red flag"] --> Indicator
  Evidence["Evidence"]
  AnalyticEvidence["Analytic evidence"] --> Evidence
  DocumentaryEvidence["Documentary evidence"] --> Evidence
  TestimonialEvidence["Testimonial evidence"] --> Evidence
  CaseStudy["CaseStudy"]
  SyntheticCaseStudy["Synthetic case study"] --> CaseStudy
  Jurisdiction["Jurisdiction"]
  NationalJurisdiction["National jurisdiction"] --> Jurisdiction
  ProjectSpecificJurisdiction["Project-specific jurisdiction"] --> Jurisdiction
  SubnationalJurisdiction["Subnational jurisdiction"] --> Jurisdiction
  GovernanceInstrument["GovernanceInstrument"]
  AuditMandate["Audit mandate"] --> GovernanceInstrument
  ContractTemplate["Contract template"] --> GovernanceInstrument
  EngineeringStandard["Engineering standard"] --> GovernanceInstrument
  IntegrityFramework["Integrity framework"] --> GovernanceInstrument
  ProcurementLaw["Procurement law"] --> GovernanceInstrument
  Sanction["Sanction"]
  AdministrativeSanction["Administrative sanction"] --> Sanction
  CivilPenalty["Civil penalty"] --> Sanction
  CriminalPenalty["Criminal penalty"] --> Sanction
  DebarmentSanction["Debarment sanction"] --> Sanction
  DetectionMechanism["DetectionMechanism"]
  AuditReviewMechanism["Audit review mechanism"] --> DetectionMechanism
  CommunityMonitoringMechanism["Community monitoring mechanism"] --> DetectionMechanism
  DataAnalyticsMechanism["Data analytics mechanism"] --> DetectionMechanism
  ReportingMechanism["ReportingMechanism"]
  AnonymousHotline["Anonymous hotline"] --> ReportingMechanism
  CitizenComplaintPortal["Citizen complaint portal"] --> ReportingMechanism
  InternalEscalationChannel["Internal escalation channel"] --> ReportingMechanism
  ProcurementMethod["ProcurementMethod"]
  EmergencyProcurementMethod["Emergency procurement method"] --> ProcurementMethod
  FrameworkAgreement["Framework agreement"] --> ProcurementMethod
  OpenTendering["Open tendering"] --> ProcurementMethod
  RestrictedTendering["Restricted tendering"] --> ProcurementMethod
  SingleSourceProcurement["Single-source procurement"] --> ProcurementMethod
  AssetOrResource["AssetOrResource"]
  BudgetAllocation["Budget allocation"] --> AssetOrResource
  ConstructionMaterial["Construction material"] --> AssetOrResource
  InspectionReport["Inspection report"] --> AssetOrResource
  LandParcel["Land parcel"] --> AssetOrResource
  PaymentCertificate["Payment certificate"] --> AssetOrResource
  ProjectInformation["Project information"] --> AssetOrResource
  DecisionPoint["DecisionPoint"]
  BidEvaluationDecisionPoint["Bid evaluation decision point"] --> DecisionPoint
  NeedsAssessmentDecisionPoint["Needs assessment decision point"] --> DecisionPoint
  PaymentCertificationDecisionPoint["Payment certification decision point"] --> DecisionPoint
  VariationApprovalDecisionPoint["Variation approval decision point"] --> DecisionPoint
  ProjectManagementProcess["ProjectManagementProcess"]
  BidEvaluationProcess["Bid evaluation process"] --> ProjectManagementProcess
  ChangeManagementProcess["Change management process"] --> ProjectManagementProcess
  ContractAdministrationProcess["Contract administration process"] --> ProjectManagementProcess
  MonitoringAndEvaluationProcess["Monitoring and evaluation process"] --> ProjectManagementProcess
  NeedsAssessmentProcess["Needs assessment process"] --> ProjectManagementProcess
  QualityInspectionProcess["Quality inspection process"] --> ProjectManagementProcess
```
