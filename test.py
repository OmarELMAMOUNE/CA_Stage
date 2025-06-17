Starting job ri.jemma.main.job.00000004-a8f1-32fb-ba25-ca0003aacebc
Cloning repository ri.stemma.main.repository.a92e072c-db52-4423-8b19-1e05a2240b17.
Cloned repository.
[Stack level override] ORG_GRADLE_PROJECT_envPackingLogicVersion=2
[Repo level override] ORG_GRADLE_PROJECT_envPackingLogicVersion=2
Picked up JAVA_TOOL_OPTIONS:  -Duser.home=/opt/palantir/services/.309060329/var/tmp/jemma-users/a4d83781696e70d8c4e23bbb8d74e517 -XX:+IgnoreUnrecognizedVMOptions --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.lang.invoke=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.util.concurrent=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.base/sun.nio.cs=ALL-UNNAMED --add-opens=java.base/sun.security.action=ALL-UNNAMED --add-opens=java.base/sun.util.calendar=ALL-UNNAMED --add-exports=jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED --add-exports=jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED --add-exports=jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED --add-exports=jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED --add-exports=jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED
Picked up _JAVA_OPTIONS:  -Djava.io.tmpdir=/opt/palantir/services/.309060329/var/tmp/jemma-users/a4d83781696e70d8c4e23bbb8d74e517/caches/TEMP/ri.jemma.main.job.00000004-a8f1-32fb-ba25-ca0003aacebc/JAVA_TMP_DIR  

> Configure project :transforms-python

	+---NOTE--------------------------------------------------+
	| To reduce checks time and improve visibility,           |
	| Conda dependency resolutions are locked.                |
	| Modify list of dependencies in conda_recipe/meta.yml    |
	| to force an update.                                     |
	+---------------------------------------------------------+


No .maestro folder found, skipping maestro plugin setup.

> Task :transforms-python:convertTrustStore
Task :convertTrustStore took 0.082 secs

> Task :transforms-python:copyHawkIntoBuildDirectory
Task :copyHawkIntoBuildDirectory took 0.025 secs

> Task :transforms-python:checkStaticInstaller
Task :checkStaticInstaller took 0.012 secs

> Task :transforms-python:extractCondaWrapper
Task :extractCondaWrapper took 0.215 secs

> Task :transforms-python:checkBackingRepositoriesPermissions
Task :checkBackingRepositoriesPermissions took 0.066 secs

> Task :transforms-python:checkMetaYaml
Task :checkMetaYaml took 0.003 secs

> Task :transforms-python:checkSharedLibraries SKIPPED
Task :checkSharedLibraries took 0.001 secs

> Task :transforms-python:condaRender
Task :condaRender took 0.291 secs

> Task :transforms-python:runCheckRecalledPackages
Task :runCheckRecalledPackages took 0.224 secs

> Task :transforms-python:condaInfo
Executing task 'condaInfo' with 'CONDA'
Task :condaInfo took 2.493 secs

> Task :transforms-python:symlinkCondaExecutable
Task :symlinkCondaExecutable took 0.006 secs

> Task :transforms-python:symlinkMambaExecutable
Task :symlinkMambaExecutable took 0.003 secs

> Task :transforms-python:setupConda
Executing task 'setupConda' with 'HAWK'
Task :setupConda took 6.801 secs

> Task :transforms-python:runVersions
Dynamically selected version is 2.345.0
Querying for pinned version for repository ri.stemma.main.repository.a92e072c-db52-4423-8b19-1e05a2240b17
No pinned transforms version found, using dynamically selected version
Successfully resolved conda versions from lock file
Task :runVersions took 0.236 secs

> Task :transforms-python:runPrintLockFile SKIPPED
Task :runPrintLockFile took 0.0 secs

> Task :transforms-python:condaPackRun
No pack entry for cache key 5cebdd20293814fd4dac4422b602e5f49f2e7f152a4ad81d4f5507b4c1fa4702, will execute pack task
Executing task 'condaPackRun' with 'HAWK'
CondaPackTask is running with hawk pack
Successfully uploaded environment to artifacts cache with key 5cebdd20293814fd4dac4422b602e5f49f2e7f152a4ad81d4f5507b4c1fa4702
Task :condaPackRun took 16.415 secs

> Task :transforms-python:runRequires
Task :runRequires took 0.003 secs

> Task :transforms-python:condaLocksPatch
Task :condaLocksPatch took 0.021 secs

> Task :transforms-python:patch
Task :patch took 0.0 secs

> Task :transforms-python:versionPy
Task :versionPy took 0.005 secs

> Task :transforms-python:prepackage
Task :prepackage took 0.0 secs

> Task :transforms-python:symlinkPythonExecutable
Task :symlinkPythonExecutable took 0.055 secs

> Task :transforms-python:condaDevelop
Task :condaDevelop took 1.051 secs

> Task :transforms-python:fetchCondaJars
Task :fetchCondaJars took 0.015 secs

> Task :transforms-python:condaRunList
Executing task 'condaRunList' with 'HAWK'
Task :condaRunList took 0.073 secs

> Task :transforms-python:renderPythonRequirementsLock
===== Beginning of used package versions =====
_libgcc_mutex=0.1=conda_forge@tar.bz2
_openmp_mutex=4.5=2_gnu@tar.bz2
aiobotocore=2.22.0=pyhd8ed1ab_0@conda
aiohappyeyeballs=2.6.1=pyhd8ed1ab_0@conda
aiohttp=3.12.4=py312h178313f_0@conda
aioitertools=0.12.0=pyhd8ed1ab_1@conda
aiosignal=1.3.2=pyhd8ed1ab_0@conda
attrs=25.3.0=pyh71513ae_0@conda
aws-c-auth=0.8.0=hb88c0a9_10@conda
aws-c-cal=0.8.0=hecf86a2_2@conda
aws-c-common=0.10.3=hb9d3cd8_0@conda
aws-c-compression=0.3.0=hf42f96a_2@conda
aws-c-event-stream=0.5.0=h1ffe551_7@conda
aws-c-http=0.9.1=hab05fe4_2@conda
aws-c-io=0.15.2=hdeadb07_2@conda
aws-c-mqtt=0.11.0=h7bd072d_8@conda
aws-c-s3=0.7.4=h3a84f74_0@conda
aws-c-sdkutils=0.2.1=hf42f96a_1@conda
aws-checksums=0.2.2=hf42f96a_1@conda
aws-crt-cpp=0.29.6=h159bff8_2@conda
aws-sdk-cpp=1.11.449=h5558e3c_4@conda
azure-core-cpp=1.14.0=h5cfcd09_0@conda
azure-identity-cpp=1.10.0=h113e628_0@conda
azure-storage-blobs-cpp=12.13.0=h3cf044e_1@conda
azure-storage-common-cpp=12.8.0=h736e048_1@conda
azure-storage-files-datalake-cpp=12.12.0=ha633028_1@conda
botocore=1.37.3=pyge310_1234567_0@conda
brotli-python=1.1.0=py312h2ec8cdc_2@conda
bzip2=1.0.8=h4bc722e_7@conda
c-ares=1.34.5=hb9d3cd8_0@conda
ca-certificates=2025.4.26=hbd8a1cb_0@conda
certifi=2025.4.26=pyhd8ed1ab_0@conda
cffi=1.17.1=py312h06ac9bb_0@conda
charset-normalizer=3.4.2=pyhd8ed1ab_0@conda
conjure-python-client=2.12.0=pyhd8ed1ab_1@conda
data-health-api=1.1162.0+5.ga0362a0=py_0@tar.bz2
decorator=5.2.1=pyhd8ed1ab_0@conda
foundry-container-sidecar-api=0.1765.0+6.g652bce3=py_0@tar.bz2
foundry-data-sidecar-api=0.836.0=py_0@tar.bz2
foundry-transforms-lib-python=0.869.0=py_0@tar.bz2
frozenlist=1.6.0=py312hb9e946c_0@conda
fsspec=2025.5.1=pyhd8ed1ab_0@conda
future=1.0.0=pyhd8ed1ab_2@conda
gflags=2.2.2=h5888daf_1005@conda
glog=0.7.1=hbabe93e_0@conda
h2=4.2.0=pyhd8ed1ab_0@conda
hpack=4.1.0=pyhd8ed1ab_0@conda
hyperframe=6.1.0=pyhd8ed1ab_0@conda
icu=75.1=he02047a_0@conda
idna=3.10=pyhd8ed1ab_1@conda
importlib-metadata=8.7.0=pyhe01879c_1@conda
jmespath=1.0.1=pyhd8ed1ab_1@conda
keyutils=1.6.1=h166bdaf_0@tar.bz2
krb5=1.21.3=h659f571_0@conda
ld_impl_linux-64=2.43=h712a8e2_4@conda
libabseil=20240722.0=cxx17_hbbce691_4@conda
libarrow-acero=18.1.0=h5888daf_1_cpu@conda
libarrow-dataset=18.1.0=h5888daf_1_cpu@conda
libarrow-substrait=18.1.0=h5c8f2c3_1_cpu@conda
libarrow=18.1.0=he15abb1_1_cpu@conda
libblas=3.9.0=31_h59b9bed_openblas@conda
libbrotlicommon=1.1.0=hb9d3cd8_2@conda
libbrotlidec=1.1.0=hb9d3cd8_2@conda
libbrotlienc=1.1.0=hb9d3cd8_2@conda
libcblas=3.9.0=31_he106b2a_openblas@conda
libcrc32c=1.1.2=h9c3ff4c_0@tar.bz2
libcurl=8.14.0=h332b0f4_0@conda
libedit=3.1.20250104=pl5321h7949ede_0@conda
libev=4.33=hd590300_2@conda
libevent=2.1.12=hf998b51_1@conda
libexpat=2.7.0=h5888daf_0@conda
libffi=3.4.6=h2dba641_1@conda
libgcc-ng=15.1.0=h69a702a_2@conda
libgcc=15.1.0=h767d61c_2@conda
libgfortran5=15.1.0=hcea5267_2@conda
libgfortran=15.1.0=h69a702a_2@conda
libgomp=15.1.0=h767d61c_2@conda
libgoogle-cloud-storage=2.31.0=h0121fbd_0@conda
libgoogle-cloud=2.31.0=h804f50b_0@conda
libgrpc=1.67.1=hc2c308b_0@conda
libiconv=1.18=h4ce23a2_1@conda
liblapack=3.9.0=31_h7ac8fdf_openblas@conda
liblzma=5.8.1=hb9d3cd8_1@conda
libnghttp2=1.64.0=h161d5f1_0@conda
libnsl=2.0.1=hd590300_0@conda
libopenblas=0.3.29=pthreads_h94d23a6_0@conda
libparquet=18.1.0=h6bd9018_1_cpu@conda
libprotobuf=5.28.2=h5b01275_0@conda
libre2-11=2024.07.02=hbbce691_2@conda
libsqlite=3.49.2=hee588c1_0@conda
libssh2=1.11.1=hcf80075_0@conda
libstdcxx-ng=15.1.0=h4852527_2@conda
libstdcxx=15.1.0=h8f9b012_2@conda
libthrift=0.21.0=h0e7cc3e_0@conda
libutf8proc=2.8.0=hf23e847_1@conda
libuuid=2.38.1=h0b41bf4_0@conda
libxcrypt=4.4.36=hd590300_1@conda
libxml2=2.13.8=h4bc477f_0@conda
libzlib=1.3.1=hb9d3cd8_2@conda
lz4-c=1.9.4=hcb278e6_0@conda
multidict=6.4.4=py312h178313f_0@conda
ncurses=6.5=h2d0b736_3@conda
numpy=1.26.4=py312heda63a1_0@conda
openssl=3.5.0=h7b32b05_1@conda
orc=2.0.3=he039a57_0@conda
packaging=25.0=pyh29332c3_1@conda
palantir-spark-time=3.24.0=py_0@tar.bz2
parsimonious=0.10.0=pyhd8ed1ab_1@conda
pip=25.1.1=pyh8b19718_0@conda
polars=1.26.0=py312hda0fa55_0@conda
propcache=0.3.1=py312h178313f_0@conda
py4j=0.10.9.7=pyhd8ed1ab_0@tar.bz2
pyaml=25.1.0=pyhd8ed1ab_0@conda
pyarrow-core=18.1.0=py312h01725c0_0_cpu@conda
pyarrow=18.1.0=py312h7900ff3_0@conda
pycparser=2.22=pyh29332c3_1@conda
pysocks=1.7.1=pyha55dd90_7@conda
pyspark-src=3.5.1.47=py_0@tar.bz2
pyspark=3.5.1.47=py_0@tar.bz2
python-dateutil=2.9.0.post0=pyhff2d567_1@conda
python=3.12.10=h9e4cc4f_0_cpython@conda
python_abi=3.12=7_cp312@conda
pytz=2025.2=pyhd8ed1ab_0@conda
pyyaml=6.0.2=py312h178313f_2@conda
re2=2024.07.02=h9925aae_2@conda
readline=8.2=h8c095d6_2@conda
regex=2024.11.6=py312h66e93f0_0@conda
requests=2.32.3=pyhd8ed1ab_1@conda
s2n=1.5.9=h0fd0ee4_0@conda
s3fs=2025.5.1=pyhd8ed1ab_0@conda
setuptools=70.0.0=pyhd8ed1ab_0@conda
six=1.17.0=pyhd8ed1ab_0@conda
snappy=1.2.1=h8bd8927_1@conda
tables-api=0.1066.0=py_0@tar.bz2
tk=8.6.13=noxft_hd72426e_102@conda
transforms-container-ops-python=0.87.0=py312@tar.bz2
transforms-expectations=0.822.0+3.g1c4f93d=py_0@tar.bz2
transforms-preview=0.822.0=py_0@tar.bz2
transforms-verbs=0.822.0+3.g1c4f93d=py_0@tar.bz2
transforms=2.345.0=py_0@tar.bz2
typeguard=4.4.2=pyhd8ed1ab_0@conda
typing-extensions=4.13.2=h0e9735f_0@conda
typing_extensions=4.13.2=pyh29332c3_0@conda
tzdata=2025b=h78e105d_0@conda
urllib3=2.4.0=pyhd8ed1ab_0@conda
wheel=0.45.1=pyhd8ed1ab_1@conda
wrapt=1.17.2=py312h66e93f0_0@conda
yaml=0.2.5=h7f98852_2@tar.bz2
yarl=1.20.0=py312h178313f_0@conda
zipp=3.22.0=pyhd8ed1ab_0@conda
zstandard=0.23.0=py312h66e93f0_2@conda
zstd=1.5.7=hb8e6e7a_2@conda
transforms-python-ri.stemma.main.repository.a92e072c-db52-4423-8b19-1e05a2240b17=0.0.1+57.gc0fccd4=py312_0@
===== End of used package versions =====
Task :renderPythonRequirementsLock took 0.016 secs

> Task :transforms-python:pythonRenderDependencyGraph
Task :pythonRenderDependencyGraph took 1.558 secs

> Task :transforms-python:checkScalaDependencies
Task :checkScalaDependencies took 0.013 secs

> Task :transforms-python:checkScalaDependenciesInsight SKIPPED
Task :checkScalaDependenciesInsight took 0.0 secs

> Task :transforms-python:check
Task :check took 0.0 secs

> Task :transforms-python:renderContainerTransformSpecs
Task :renderContainerTransformSpecs took 0.09 secs

> Task :transforms-python:renderDependencyGraph
Task :renderDependencyGraph took 0.0 secs

> Task :checkShrinkwrap FAILED
Task :checkShrinkwrap took 0.062 secs


************************************************************************
Input/output paths must be absolute. Found input/output with invalid path '"SOURCE_DATASET_PATH"' in files ["transforms-python/src/myproject/datasets/DC-CIV-OEM/PRETRAITEMENT/5_executions_client_1month_oem.py"].
************************************************************************


== Build time summary ==
:transforms-python:condaPackRun                        | SUCCESS    | 16.416 secs
:transforms-python:setupConda                          | SUCCESS    | 6.801 secs
:transforms-python:condaInfo                           | SUCCESS    | 2.493 secs
:transforms-python:pythonRenderDependencyGraph         | SUCCESS    | 1.558 secs
:transforms-python:condaDevelop                        | SUCCESS    | 1.052 secs
:transforms-python:condaRender                         | SUCCESS    | 0.291 secs
:transforms-python:runVersions                         | SUCCESS    | 0.237 secs
:transforms-python:runCheckRecalledPackages            | SUCCESS    | 0.225 secs
:transforms-python:extractCondaWrapper                 | SUCCESS    | 0.216 secs
:transforms-python:renderContainerTransformSpecs       | SUCCESS    | 0.091 secs
:transforms-python:convertTrustStore                   | SUCCESS    | 0.085 secs
:transforms-python:condaRunList                        | SUCCESS    | 0.073 secs
:transforms-python:checkBackingRepositoriesPermissions | SUCCESS    | 0.066 secs
:transforms-python:symlinkPythonExecutable             | SUCCESS    | 0.055 secs
:transforms-python:copyHawkIntoBuildDirectory          | SUCCESS    | 0.025 secs
:transforms-python:condaLocksPatch                     | SUCCESS    | 0.021 secs
:transforms-python:renderPythonRequirementsLock        | SUCCESS    | 0.016 secs
:transforms-python:fetchCondaJars                      | SUCCESS    | 0.015 secs
:transforms-python:checkScalaDependencies              | SUCCESS    | 0.013 secs
:transforms-python:checkStaticInstaller                | SUCCESS    | 0.012 secs
:transforms-python:symlinkCondaExecutable              | SUCCESS    | 0.006 secs
:transforms-python:versionPy                           | SUCCESS    | 0.005 secs
:transforms-python:runRequires                         | SUCCESS    | 0.004 secs
:transforms-python:symlinkMambaExecutable              | SUCCESS    | 0.003 secs
:transforms-python:checkMetaYaml                       | SUCCESS    | 0.003 secs
:transforms-python:checkSharedLibraries                | SKIPPED    | 0.001 secs
:transforms-python:runPrintLockFile                    | SKIPPED    | 0.0 secs
:transforms-python:check                               | UNKNOWN    | 0.0 secs
:transforms-python:prepackage                          | UNKNOWN    | 0.0 secs
:transforms-python:patch                               | UNKNOWN    | 0.0 secs
:transforms-python:checkScalaDependenciesInsight       | SKIPPED    | 0.0 secs
:transforms-python:renderDependencyGraph               | UNKNOWN    | 0.0 secs
:checkShrinkwrap                                       | FAILED     | 0.076 secs

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':checkShrinkwrap'.
> ChecksException: (Shrinkwrap:DefaultPathNotAbsolute): {locations=["transforms-python/src/myproject/datasets/DC-CIV-OEM/PRETRAITEMENT/5_executions_client_1month_oem.py"], defaultPath="SOURCE_DATASET_PATH"}

* Try:
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.

* Exception is:
org.gradle.api.tasks.TaskExecutionException: Execution failed for task ':checkShrinkwrap'.
	at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.lambda$executeIfValid$1(ExecuteActionsTaskExecuter.java:142)
	at org.gradle.internal.Try$Failure.ifSuccessfulOrElse(Try.java:282)
	at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.executeIfValid(ExecuteActionsTaskExecuter.java:140)
	at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.execute(ExecuteActionsTaskExecuter.java:128)
	at org.gradle.api.internal.tasks.execution.CleanupStaleOutputsExecuter.execute(CleanupStaleOutputsExecuter.java:77)
	at org.gradle.api.internal.tasks.execution.FinalizePropertiesTaskExecuter.execute(FinalizePropertiesTaskExecuter.java:46)
	at org.gradle.api.internal.tasks.execution.ResolveTaskExecutionModeExecuter.execute(ResolveTaskExecutionModeExecuter.java:51)
	at org.gradle.api.internal.tasks.execution.SkipTaskWithNoActionsExecuter.execute(SkipTaskWithNoActionsExecuter.java:57)
	at org.gradle.api.internal.tasks.execution.SkipOnlyIfTaskExecuter.execute(SkipOnlyIfTaskExecuter.java:57)
	at org.gradle.api.internal.tasks.execution.CatchExceptionTaskExecuter.execute(CatchExceptionTaskExecuter.java:36)
	at org.gradle.api.internal.tasks.execution.EventFiringTaskExecuter$1.executeTask(EventFiringTaskExecuter.java:77)
	at org.gradle.api.internal.tasks.execution.EventFiringTaskExecuter$1.call(EventFiringTaskExecuter.java:55)
	at org.gradle.api.internal.tasks.execution.EventFiringTaskExecuter$1.call(EventFiringTaskExecuter.java:52)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$CallableBuildOperationWorker.execute(DefaultBuildOperationRunner.java:204)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$CallableBuildOperationWorker.execute(DefaultBuildOperationRunner.java:199)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:66)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:59)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:157)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:59)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.call(DefaultBuildOperationRunner.java:53)
	at org.gradle.internal.operations.DefaultBuildOperationExecutor.call(DefaultBuildOperationExecutor.java:73)
	at org.gradle.api.internal.tasks.execution.EventFiringTaskExecuter.execute(EventFiringTaskExecuter.java:52)
	at org.gradle.execution.plan.LocalTaskNodeExecutor.execute(LocalTaskNodeExecutor.java:69)
	at org.gradle.execution.taskgraph.DefaultTaskExecutionGraph$InvokeNodeExecutorsAction.execute(DefaultTaskExecutionGraph.java:322)
	at org.gradle.execution.taskgraph.DefaultTaskExecutionGraph$InvokeNodeExecutorsAction.execute(DefaultTaskExecutionGraph.java:309)
	at org.gradle.execution.taskgraph.DefaultTaskExecutionGraph$BuildOperationAwareExecutionAction.execute(DefaultTaskExecutionGraph.java:302)
	at org.gradle.execution.taskgraph.DefaultTaskExecutionGraph$BuildOperationAwareExecutionAction.execute(DefaultTaskExecutionGraph.java:288)
	at org.gradle.execution.plan.DefaultPlanExecutor$ExecutorWorker.execute(DefaultPlanExecutor.java:462)
	at org.gradle.execution.plan.DefaultPlanExecutor$ExecutorWorker.run(DefaultPlanExecutor.java:379)
	at org.gradle.internal.concurrent.ExecutorPolicy$CatchAndRecordFailures.onExecute(ExecutorPolicy.java:64)
	at org.gradle.internal.concurrent.ManagedExecutorImpl$1.run(ManagedExecutorImpl.java:49)
Caused by: com.palantir.transforms.gradle.api.ChecksException: ChecksException: (Shrinkwrap:DefaultPathNotAbsolute): {locations=["transforms-python/src/myproject/datasets/DC-CIV-OEM/PRETRAITEMENT/5_executions_client_1month_oem.py"], defaultPath="SOURCE_DATASET_PATH"}
	at com.palantir.transforms.gradle.api.TransformsPreconditions.checkArgument(TransformsPreconditions.java:24)
	at com.palantir.transforms.shrinkwrap.core.UnresolvedShrinkwrapMapping.check(UnresolvedShrinkwrapMapping.java:71)
	at com.palantir.transforms.shrinkwrap.core.ImmutableUnresolvedShrinkwrapMapping.validate(ImmutableUnresolvedShrinkwrapMapping.java:356)
	at com.palantir.transforms.shrinkwrap.core.ImmutableUnresolvedShrinkwrapMapping$Builder.build(ImmutableUnresolvedShrinkwrapMapping.java:613)
	at com.palantir.transforms.gradle.tasks.CheckShrinkwrap.lambda$checkShrinkwrap$0(CheckShrinkwrap.java:167)
	at com.google.common.collect.CollectSpliterators$1.lambda$forEachRemaining$0(CollectSpliterators.java:124)
	at com.google.common.collect.CollectSpliterators$1.forEachRemaining(CollectSpliterators.java:124)
	at com.palantir.transforms.gradle.tasks.CheckShrinkwrap.checkShrinkwrap(CheckShrinkwrap.java:153)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:77)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at org.gradle.internal.reflect.JavaMethod.invoke(JavaMethod.java:125)
	at org.gradle.api.internal.project.taskfactory.StandardTaskAction.doExecute(StandardTaskAction.java:58)
	at org.gradle.api.internal.project.taskfactory.StandardTaskAction.execute(StandardTaskAction.java:51)
	at org.gradle.api.internal.project.taskfactory.StandardTaskAction.execute(StandardTaskAction.java:29)
	at org.gradle.api.internal.tasks.execution.TaskExecution$3.run(TaskExecution.java:236)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$1.execute(DefaultBuildOperationRunner.java:29)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$1.execute(DefaultBuildOperationRunner.java:26)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:66)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:59)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:157)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:59)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.run(DefaultBuildOperationRunner.java:47)
	at org.gradle.internal.operations.DefaultBuildOperationExecutor.run(DefaultBuildOperationExecutor.java:68)
	at org.gradle.api.internal.tasks.execution.TaskExecution.executeAction(TaskExecution.java:221)
	at org.gradle.api.internal.tasks.execution.TaskExecution.executeActions(TaskExecution.java:204)
	at org.gradle.api.internal.tasks.execution.TaskExecution.executeWithPreviousOutputFiles(TaskExecution.java:187)
	at org.gradle.api.internal.tasks.execution.TaskExecution.execute(TaskExecution.java:165)
	at org.gradle.internal.execution.steps.ExecuteStep.executeInternal(ExecuteStep.java:89)
	at org.gradle.internal.execution.steps.ExecuteStep.access$000(ExecuteStep.java:40)
	at org.gradle.internal.execution.steps.ExecuteStep$1.call(ExecuteStep.java:53)
	at org.gradle.internal.execution.steps.ExecuteStep$1.call(ExecuteStep.java:50)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$CallableBuildOperationWorker.execute(DefaultBuildOperationRunner.java:204)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$CallableBuildOperationWorker.execute(DefaultBuildOperationRunner.java:199)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:66)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:59)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:157)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:59)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.call(DefaultBuildOperationRunner.java:53)
	at org.gradle.internal.operations.DefaultBuildOperationExecutor.call(DefaultBuildOperationExecutor.java:73)
	at org.gradle.internal.execution.steps.ExecuteStep.execute(ExecuteStep.java:50)
	at org.gradle.internal.execution.steps.ExecuteStep.execute(ExecuteStep.java:40)
	at org.gradle.internal.execution.steps.RemovePreviousOutputsStep.execute(RemovePreviousOutputsStep.java:68)
	at org.gradle.internal.execution.steps.RemovePreviousOutputsStep.execute(RemovePreviousOutputsStep.java:38)
	at org.gradle.internal.execution.steps.CancelExecutionStep.execute(CancelExecutionStep.java:41)
	at org.gradle.internal.execution.steps.TimeoutStep.executeWithoutTimeout(TimeoutStep.java:74)
	at org.gradle.internal.execution.steps.TimeoutStep.execute(TimeoutStep.java:55)
	at org.gradle.internal.execution.steps.CreateOutputsStep.execute(CreateOutputsStep.java:51)
	at org.gradle.internal.execution.steps.CreateOutputsStep.execute(CreateOutputsStep.java:29)
	at org.gradle.internal.execution.steps.CaptureStateAfterExecutionStep.executeDelegateBroadcastingChanges(CaptureStateAfterExecutionStep.java:124)
	at org.gradle.internal.execution.steps.CaptureStateAfterExecutionStep.execute(CaptureStateAfterExecutionStep.java:80)
	at org.gradle.internal.execution.steps.CaptureStateAfterExecutionStep.execute(CaptureStateAfterExecutionStep.java:58)
	at org.gradle.internal.execution.steps.ResolveInputChangesStep.execute(ResolveInputChangesStep.java:48)
	at org.gradle.internal.execution.steps.ResolveInputChangesStep.execute(ResolveInputChangesStep.java:36)
	at org.gradle.internal.execution.steps.BuildCacheStep.executeWithoutCache(BuildCacheStep.java:181)
	at org.gradle.internal.execution.steps.BuildCacheStep.lambda$execute$1(BuildCacheStep.java:71)
	at org.gradle.internal.Either$Right.fold(Either.java:175)
	at org.gradle.internal.execution.caching.CachingState.fold(CachingState.java:59)
	at org.gradle.internal.execution.steps.BuildCacheStep.execute(BuildCacheStep.java:69)
	at org.gradle.internal.execution.steps.BuildCacheStep.execute(BuildCacheStep.java:47)
	at org.gradle.internal.execution.steps.StoreExecutionStateStep.execute(StoreExecutionStateStep.java:36)
	at org.gradle.internal.execution.steps.StoreExecutionStateStep.execute(StoreExecutionStateStep.java:25)
	at org.gradle.internal.execution.steps.RecordOutputsStep.execute(RecordOutputsStep.java:36)
	at org.gradle.internal.execution.steps.RecordOutputsStep.execute(RecordOutputsStep.java:22)
	at org.gradle.internal.execution.steps.SkipUpToDateStep.executeBecause(SkipUpToDateStep.java:110)
	at org.gradle.internal.execution.steps.SkipUpToDateStep.lambda$execute$2(SkipUpToDateStep.java:56)
	at org.gradle.internal.execution.steps.SkipUpToDateStep.execute(SkipUpToDateStep.java:56)
	at org.gradle.internal.execution.steps.SkipUpToDateStep.execute(SkipUpToDateStep.java:38)
	at org.gradle.internal.execution.steps.ResolveChangesStep.execute(ResolveChangesStep.java:73)
	at org.gradle.internal.execution.steps.ResolveChangesStep.execute(ResolveChangesStep.java:44)
	at org.gradle.internal.execution.steps.legacy.MarkSnapshottingInputsFinishedStep.execute(MarkSnapshottingInputsFinishedStep.java:37)
	at org.gradle.internal.execution.steps.legacy.MarkSnapshottingInputsFinishedStep.execute(MarkSnapshottingInputsFinishedStep.java:27)
	at org.gradle.internal.execution.steps.ResolveCachingStateStep.execute(ResolveCachingStateStep.java:89)
	at org.gradle.internal.execution.steps.ResolveCachingStateStep.execute(ResolveCachingStateStep.java:50)
	at org.gradle.internal.execution.steps.ValidateStep.execute(ValidateStep.java:102)
	at org.gradle.internal.execution.steps.ValidateStep.execute(ValidateStep.java:57)
	at org.gradle.internal.execution.steps.CaptureStateBeforeExecutionStep.execute(CaptureStateBeforeExecutionStep.java:76)
	at org.gradle.internal.execution.steps.CaptureStateBeforeExecutionStep.execute(CaptureStateBeforeExecutionStep.java:50)
	at org.gradle.internal.execution.steps.SkipEmptyWorkStep.executeWithNoEmptySources(SkipEmptyWorkStep.java:254)
	at org.gradle.internal.execution.steps.SkipEmptyWorkStep.executeWithNoEmptySources(SkipEmptyWorkStep.java:209)
	at org.gradle.internal.execution.steps.SkipEmptyWorkStep.execute(SkipEmptyWorkStep.java:88)
	at org.gradle.internal.execution.steps.SkipEmptyWorkStep.execute(SkipEmptyWorkStep.java:56)
	at org.gradle.internal.execution.steps.RemoveUntrackedExecutionStateStep.execute(RemoveUntrackedExecutionStateStep.java:32)
	at org.gradle.internal.execution.steps.RemoveUntrackedExecutionStateStep.execute(RemoveUntrackedExecutionStateStep.java:21)
	at org.gradle.internal.execution.steps.legacy.MarkSnapshottingInputsStartedStep.execute(MarkSnapshottingInputsStartedStep.java:38)
	at org.gradle.internal.execution.steps.LoadPreviousExecutionStateStep.execute(LoadPreviousExecutionStateStep.java:43)
	at org.gradle.internal.execution.steps.LoadPreviousExecutionStateStep.execute(LoadPreviousExecutionStateStep.java:31)
	at org.gradle.internal.execution.steps.AssignWorkspaceStep.lambda$execute$0(AssignWorkspaceStep.java:40)
	at org.gradle.api.internal.tasks.execution.TaskExecution$4.withWorkspace(TaskExecution.java:281)
	at org.gradle.internal.execution.steps.AssignWorkspaceStep.execute(AssignWorkspaceStep.java:40)
	at org.gradle.internal.execution.steps.AssignWorkspaceStep.execute(AssignWorkspaceStep.java:30)
	at org.gradle.internal.execution.steps.IdentityCacheStep.execute(IdentityCacheStep.java:37)
	at org.gradle.internal.execution.steps.IdentityCacheStep.execute(IdentityCacheStep.java:27)
	at org.gradle.internal.execution.steps.IdentifyStep.execute(IdentifyStep.java:44)
	at org.gradle.internal.execution.steps.IdentifyStep.execute(IdentifyStep.java:33)
	at org.gradle.internal.execution.impl.DefaultExecutionEngine$1.execute(DefaultExecutionEngine.java:76)
	at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.executeIfValid(ExecuteActionsTaskExecuter.java:139)
	at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.execute(ExecuteActionsTaskExecuter.java:128)
	at org.gradle.api.internal.tasks.execution.CleanupStaleOutputsExecuter.execute(CleanupStaleOutputsExecuter.java:77)
	at org.gradle.api.internal.tasks.execution.FinalizePropertiesTaskExecuter.execute(FinalizePropertiesTaskExecuter.java:46)
	at org.gradle.api.internal.tasks.execution.ResolveTaskExecutionModeExecuter.execute(ResolveTaskExecutionModeExecuter.java:51)
	at org.gradle.api.internal.tasks.execution.SkipTaskWithNoActionsExecuter.execute(SkipTaskWithNoActionsExecuter.java:57)
	at org.gradle.api.internal.tasks.execution.SkipOnlyIfTaskExecuter.execute(SkipOnlyIfTaskExecuter.java:57)
	at org.gradle.api.internal.tasks.execution.CatchExceptionTaskExecuter.execute(CatchExceptionTaskExecuter.java:36)
	at org.gradle.api.internal.tasks.execution.EventFiringTaskExecuter$1.executeTask(EventFiringTaskExecuter.java:77)
	at org.gradle.api.internal.tasks.execution.EventFiringTaskExecuter$1.call(EventFiringTaskExecuter.java:55)
	at org.gradle.api.internal.tasks.execution.EventFiringTaskExecuter$1.call(EventFiringTaskExecuter.java:52)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$CallableBuildOperationWorker.execute(DefaultBuildOperationRunner.java:204)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$CallableBuildOperationWorker.execute(DefaultBuildOperationRunner.java:199)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:66)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:59)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:157)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:59)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.call(DefaultBuildOperationRunner.java:53)
	at org.gradle.internal.operations.DefaultBuildOperationExecutor.call(DefaultBuildOperationExecutor.java:73)
	at org.gradle.api.internal.tasks.execution.EventFiringTaskExecuter.execute(EventFiringTaskExecuter.java:52)
	at org.gradle.execution.plan.LocalTaskNodeExecutor.execute(LocalTaskNodeExecutor.java:69)
	at org.gradle.execution.taskgraph.DefaultTaskExecutionGraph$InvokeNodeExecutorsAction.execute(DefaultTaskExecutionGraph.java:322)
	at org.gradle.execution.taskgraph.DefaultTaskExecutionGraph$InvokeNodeExecutorsAction.execute(DefaultTaskExecutionGraph.java:309)
	at org.gradle.execution.taskgraph.DefaultTaskExecutionGraph$BuildOperationAwareExecutionAction.execute(DefaultTaskExecutionGraph.java:302)
	at org.gradle.execution.taskgraph.DefaultTaskExecutionGraph$BuildOperationAwareExecutionAction.execute(DefaultTaskExecutionGraph.java:288)
	at org.gradle.execution.plan.DefaultPlanExecutor$ExecutorWorker.execute(DefaultPlanExecutor.java:462)
	at org.gradle.execution.plan.DefaultPlanExecutor$ExecutorWorker.run(DefaultPlanExecutor.java:379)
	at org.gradle.internal.concurrent.ExecutorPolicy$CatchAndRecordFailures.onExecute(ExecutorPolicy.java:64)
	at org.gradle.internal.concurrent.ManagedExecutorImpl$1.run(ManagedExecutorImpl.java:49)


* Get more help at https://help.gradle.org

Deprecated Gradle features were used in this build, making it incompatible with Gradle 8.0.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

See https://docs.gradle.org/7.6.4/userguide/command_line_interface.html#sec:command_line_warnings

BUILD FAILED in 35s
26 actionable tasks: 26 executed