graph RL
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

    AutomatedTesting --> | BetterTogetherWith| ExploratoryTesting
    AutomatedTesting --> | BetterTogetherWith | CodeQualityScans
    AutomatedTesting --> | ReducesFailureOf | ContinuousIntegration
    UnitTesting --> | Enables | ContinuousIntegration
    CodeQualityScans --> | BetterTogetherWith | AgileWork
    CodeQualityScans --> | BetterTogetherWith | AutomatedTesting
    AgileWork --> | ReducesFailureOf | TestDrivenDevelopment
    AgileWork --> | Enables | BranchingStrategy
    BranchingStrategy --> | Enables | RepositoryComposition
    BranchingStrategy --> | Enables | ParametrisedInfrastructureasCode
    BranchingStrategy --> | ReducesFailureOf | ContinuousIntegration
    BranchingStrategy --> | ReducesFailureOf | InfrastructureasCode
    InfrastructureasCode --> | Enables | ContinuousDelivery
    InfrastructureasCode --> | Enables | ParametrisedInfrastructureasCode
    InfrastructureasCode --> | ReducesFailureOf | ContinuousDelivery
    InfrastructureasCode --> | ReducesFailureOf | ParametrisedInfrastructureasCode
    DarkLaunching --> | ReducesFailureOf | ContinuousDeployment
    TestDrivenDevelopment --> | ReducesFailureOf | UnitTesting
    TestDrivenDevelopment --> | ReducesFailureOf | AutomatedTesting
    ExploratoryTesting --> | BetterTogetherWith | AutomatedTesting
    ContinuousIntegration --> | Enables | ContinuousDelivery
    ContinuousIntegration --> | Enables | ImmutableArtefacts
    SemanticVersioning --> | Enables | ReleaseViews
    SemanticVersioning --> | ReducesFailureOf | ImmutableArtefacts
    ReleaseViews --> | ReducesFailureOf | SemanticVersioning
    ReleaseViews --> | Enables | SeparationofinternalversioningfromMarketingversioning
    ImmutableArtefacts --> | ReducesFailureOf | ContinuousIntegration
    ImmutableArtefacts --> | Enables | SemanticVersioning
    ContainerisedApplication --> | ReducesFailureOf | ContinuousDeployment
    ContinuousDelivery --> | Enables | ContinuousDeployment
    ContinuousDelivery --> | Enables | ContainerisedApplication
    SecretsVault --> | BetterTogetherWith | ContinuousDelivery
    SecretsVault --> | BetterTogetherWith | ContinuousDeployment
    ContinuousDeployment --> | Enables | DarkLaunching
    ContinuousDeployment --> | Enables | CropsnotGardenplants
    ContinuousDeployment --> | Enables | CanaryReleases
    ContinuousDeployment --> | Enables | Blue/GreenDeployment
    ContinuousDeployment --> | Enables | MicroserviceEcosystem
    ContinuousDeployment --> | BetterTogetherWith | SecretsVault
    FeatureToggles --> | ReducesFailureOf | MicroserviceEcosystem
    FeatureToggles --> | BetterTogetherWith | ConfigDatabase/Git
    ConfigDatabase/Git --> | BetterTogetherWith | FeatureToggles
    ChaosAgent --> | ReducesFailureOf | ContinuousDeployment
    CropsnotGardenplants --> | ReducesFailureOf | ContinuousDeployment
