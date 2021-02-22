flowchart TB
    AgileWork(Agile Work)
    AutomatedTesting(Automated Testing)
    Blue/GreenDeployment(Blue/Green Deployment)
    BranchingStrategy(Branching Strategy)
    CanaryReleases(Canary Releases)
    ChaosAgent(Chaos Agent)
    CodeQualityScans(Code Quality Scans)
    CodeQualityScans(Code Quality Scans)
    ConfigDatabase/Git(Config Database/Git)
    ContainerisedApplication(Containerised Application)
    ContinuousDelivery(Continuous Delivery)
    ContinuousDeployment(Continuous Deployment)
    ContinuousIntegration(Continuous Integration)
    CropsnotGardenplants(Crops not Garden plants)
    DarkLaunching(Dark Launching)
    ExploratoryTesting(Exploratory Testing)
    FeatureToggles(Feature Toggles)
    ImmutableArtefacts(Immutable Artefacts)
    InfrastructureasCode(Infrastructure as Code)
    MicroserviceEcosystem(Microservice Ecosystem)
    ParametrisedInfrastructureasCode(Parametrised Infrastructure as Code)
    ReleaseViews(Release Views)
    RepositoryComposition(Repository Composition)
    SecretsVault(Secrets Vault)
    SemanticVersioning(Semantic Versioning)
    SeparationofinternalversioningfromMarketingversioning(Separation of internal versioning from Marketing versioning)
    TestDrivenDevelopment(Test Driven Development)
    UnitTesting(Unit Testing)

    AutomatedTesting  <-. Better Together With  .-> ExploratoryTesting
    AutomatedTesting  <-. Better Together With  .-> CodeQualityScans
    AutomatedTesting .-> | Reduces Failure Of | ContinuousIntegration
    UnitTesting --> | Enables | ContinuousIntegration
    CodeQualityScans  <-. Better Together With  .-> AgileWork
    AgileWork .-> | Reduces Failure Of | TestDrivenDevelopment
    AgileWork --> | Enables | BranchingStrategy
    BranchingStrategy --> | Enables | RepositoryComposition
    BranchingStrategy --> | Enables | ParametrisedInfrastructureasCode
    BranchingStrategy .-> | Reduces Failure Of | ContinuousIntegration
    BranchingStrategy .-> | Reduces Failure Of | InfrastructureasCode
    InfrastructureasCode --> | Enables | ContinuousDelivery
    InfrastructureasCode --> | Enables | ParametrisedInfrastructureasCode
    InfrastructureasCode .-> | Reduces Failure Of | ContinuousDelivery
    InfrastructureasCode .-> | Reduces Failure Of | ParametrisedInfrastructureasCode
    DarkLaunching .-> | Reduces Failure Of | ContinuousDeployment
    TestDrivenDevelopment .-> | Reduces Failure Of | UnitTesting
    TestDrivenDevelopment .-> | Reduces Failure Of | AutomatedTesting
    ContinuousIntegration --> | Enables | ContinuousDelivery
    ContinuousIntegration --> | Enables | ImmutableArtefacts
    SemanticVersioning --> | Enables | ReleaseViews
    SemanticVersioning .-> | Reduces Failure Of | ImmutableArtefacts
    ReleaseViews .-> | Reduces Failure Of | SemanticVersioning
    ReleaseViews --> | Enables | SeparationofinternalversioningfromMarketingversioning
    ImmutableArtefacts .-> | Reduces Failure Of | ContinuousIntegration
    ImmutableArtefacts --> | Enables | SemanticVersioning
    ContainerisedApplication .-> | Reduces Failure Of | ContinuousDeployment
    ContinuousDelivery --> | Enables | ContinuousDeployment
    ContinuousDelivery --> | Enables | ContainerisedApplication
    SecretsVault  <-. Better Together With  .-> ContinuousDelivery
    SecretsVault  <-. Better Together With  .-> ContinuousDeployment
    ContinuousDeployment --> | Enables | DarkLaunching
    ContinuousDeployment --> | Enables | CropsnotGardenplants
    ContinuousDeployment --> | Enables | CanaryReleases
    ContinuousDeployment --> | Enables | Blue/GreenDeployment
    ContinuousDeployment --> | Enables | MicroserviceEcosystem
    FeatureToggles .-> | Reduces Failure Of | MicroserviceEcosystem
    FeatureToggles  <-. Better Together With  .-> ConfigDatabase/Git
    ChaosAgent .-> | Reduces Failure Of | ContinuousDeployment
    CropsnotGardenplants .-> | Reduces Failure Of | ContinuousDeployment
