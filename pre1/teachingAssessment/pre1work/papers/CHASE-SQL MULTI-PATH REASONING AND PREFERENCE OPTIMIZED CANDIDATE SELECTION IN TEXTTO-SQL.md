## Page 1

PublishedasaconferencepaperatICLR2025
CHASE-SQL: MULTI-PATH REASONING AND PREF-
ERENCE OPTIMIZED CANDIDATE SELECTION IN TEXT-
TO-SQL
MohammadrezaPourreza1∗,HailongLi1∗,RuoxiSun1,YeounohChung1,ShayanTalaei2,
GauravTarlokKakkar1,YuGan1,AminSaberi2,FatmaO¨zcan1,SercanO¨.Arık1
1GoogleCloud,Sunnyvale,CA,USA
2StanfordUniversity,Stanford,CA,USA
{pourreza, hailongli, ruoxis, yeounoh}@google.com
{gkakkar, gany, fozcan, soarik}@google.com
{stalaei, saberi}@stanford.edu
∗Equalcontribution
ABSTRACT
We present CHASE-SQL, a novel framework addressing large language model
(LLM) performance challenges for Text-to-SQL tasks by leveraging multi-agent
modelingandtest-timecomputeforimprovedcandidategenerationandselection.
CHASE-SQLusesLLMstogeneratediverseSQLcandidateswith: (1)adivide-
and-conquerapproachtobreakdowncomplexqueries, (2)chain-of-thoughtrea-
soningbasedonqueryexecutionplans,and(3)instance-awaresyntheticexample
generation for tailored few-shot demonstrations. A selection agent ranks candi-
datesviapairwisecomparisonsusingafine-tunedbinaryselectionLLM,offering
robust performance. This framework improves SQL query quality and diversity,
achievingstate-of-the-artexecutionaccuracyof73.0%ontheBIRDText-to-SQL
benchmarktestset,toppingtheleaderboardatthetimeofsubmission.
1 INTRODUCTION
Text-to-SQL, as a bridge between human language and machine-readable structured query lan-
guages, is crucial for many use cases, converting natural language questions into executable SQL
commands (Androutsopoulos et al., 1995; Hristidis et al., 2003; Li & Jagadish, 2014; Li et al.,
2024c;Yuetal.,2018).Byenablinguserstointeractwithcomplexdatabasesystemswithoutrequir-
ingSQLproficiency,Text-to-SQLempowersuserstoextractvaluableinsights,performstreamlined
data exploration, make informed decisions, generate data-driven reports and mine better features
for machine learning (Wang et al., 2019; Pourreza & Rafiei, 2024a; Sun et al., 2023; Chen et al.,
2023;Pourrezaetal.,2024;Pe´rez-Mercadoetal.,2023;Xieetal.,2023).Furthermore,Text-to-SQL
systemsplayapivotalroleinautomatingdataanalyticswithcomplexreasoningandpoweringcon-
versational agents, expanding their applications beyond traditional data retrieval (Sun et al., 2023;
Xieetal.,2023). Asdatacontinuestogrowexponentially,theabilitytoquerydatabasesefficiently
withoutextensiveSQLknowledgebecomesincreasinglyvitalforabroadrangeofapplications.
Text-to-SQLcanbeconsideredaspecializedformofcodegeneration,withthecontextualinforma-
tionpotentiallyincludingthedatabaseschema,itsmetadataandalongwiththevalues.Inthebroader
codegenerationdomain, utilizingLLMstogenerateawiderangeofdiversecandidatesandselect
the best one has proven to be effective (Li et al., 2022; Ni et al., 2023; Chen et al., 2021). How-
ever,itisnon-obviouswhatleadstomosteffectivecandidateproposalandwinnerselectormecha-
nisms.Astraightforwardyeteffectiveapproachinvolvesgeneratingcandidatesusingzero-/few-shot
or open-ended prompting, followed by selecting the best options utilizing self-consistency (Wang
et al., 2022), which entails clustering candidates based on their execution outputs. This approach
hasdemonstratedpromisingresultsinseveralstudies(Maamarietal.,2024;Talaeietal.,2024;Lee
etal.,2024;Wangetal.,2023). However,asinglepromptdesignmightnotfullyunleashtheexten-
siveText-to-SQLknowledgeofLLMs,andself-consistencymethodsmightnotbealwayseffective.
1

## Page 2

PublishedasaconferencepaperatICLR2025
Infact,asillustratedinTable1,themostconsistentanswerswouldnotalwaysbethecorrectones,
with an upper-bound performance 14% higher than that achieved through self-consistency. This
substantialgaphighlightsthepotentialforsignificantimprovementbyimplementingmoreeffective
selectionmethodstoidentifythebestanswerfromthepoolofcandidatequeries.
Building on the challenges outlined in the previous sec-
tion, we propose novel approaches to improve LLM Table 1: Evaluating single-query gen-
performance for Text-to-SQL by leveraging judiciously- eration vs. ensemble methods of self-
designedtest-timecomputationsinanagenticframework. consistency and the upper bound that can
As indicated by the upper bound in Table 1, utilizing be achieved for Text-to-SQL with Gemini
LLMs’intrinsicknowledgeofferssignificantpotentialfor 1.5ProontheBIRDdevset.EXstandsfor
improvement.Weproposemethodsthatgenerateadiverse executionaccuracy.
setofhigh-qualitycandidateresponsesandapplyaselec-
tion mechanism to identify the best answer. Achieving Method EX(%)
bothhigh-qualityanddiversecandidateresponsesiscrit- Singlequery 63.01
ical for the success of scoring-based selection methods. Self-consistency 68.84(+5.84)
Upper-bound 82.79(+19.78)
Low diversity limits improvement potential and reduces
thedifferencebetweenself-consistencyandscoring-based
approaches. Whiletechniqueslikeincreasingtemperatureorreorderingpromptcontentscanboost
diversity, they often compromise the quality of the candidates. To address this, we introduce ef-
fectivecandidategeneratorsdesignedtoenhancediversitywhilemaintaininghigh-qualityoutputs.
Specifically, we propose three distinct candidate generation approaches, each capable of produc-
inghigh-qualityresponses. Thefirstisinspiredbythedivide-and-conqueralgorithm,whichbreaks
down complex problems into smaller, manageable parts to handle difficult queries. The second
employsaqueryexecution-plan-basedchain-of-thoughtstrategy,wherethereasoningprocessmir-
rorsthestepsadatabaseenginetakesduringqueryexecution. Lastly, weintroduceanovelonline
syntheticexamplegenerationmethod,whichhelpsthemodelbetterunderstandtheunderlyingdata
schemaofthetestdatabase. Thesemethods,whenusedindependently,canproducehighly-accurate
SQLoutputs.Toeffectivelyselectthebestansweramongcandidates,weintroduceaselectionagent,
trained with a classification objective, that assigns scores based on pairwise comparisons between
candidatequeries. Withthisagent, weconstructacomparisonmatrixforallcandidatesandselect
the final response based on the highest cumulative score. By combining these candidate genera-
tionmethodswiththeproposedscoringmodel,wecreateanensembleapproachthatleveragesthe
strengthsofeachstrategytosignificantlyimproveoverallperformance.
WepresentcomprehensiveevaluationsontheefficacyofproposedmethodologiesofCHASE-SQL.
Ourinnovativecandidategenerationapproachesdemonstratesuperiorperformancecomparedtotra-
ditionalgenericCoTprompts,illustratingtheircapabilityinguidingLLMsthroughthedecomposi-
tionofcomplexproblemsintomanageableintermediatesteps. Furthermore,theproposedselection
agentsignificantlyoutperformsconventionalconsistency-basedmethods, contributingtothestate-
of-the-artresults. Specifically,CHASE-SQLreachesanexecutionaccuracyof73.01%and73.0%
onthedevelopmentsetandtestsetofthechallengingBIRDText-to-SQLdatasetwhichoutperforms
allofthepublishedandundisclosedmethodsonthisbenchmark,byalargemargin. Moreover,by
leveragingentirelyopen-sourcemodels—MistralLargeModel(AI,2024)asthecandidategenera-
tor and a fine-tuned Qwen-2.5-coder model (Team, 2024) as the selector—our method achieved a
state-of-the-artperformanceof70.33ontheBIRDdevelopmentsetwithopen-sourcemodels.
2 METHODS
2.1 OVERALLFRAMEWORK
This section outlines the proposed CHASE-SQL framework, which consists of four primary com-
ponents: 1) Value retrieval, 2) Candidate generator, 3) Query fixer, and 4) Selection agent. As
illustratedinFig. 1. Theproposedframeworkbeginsbyretrievingrelevantdatabasevalues. Sub-
sequently,allcontextualinformation,includingretrievedvalues,databasemetadata,andschema,is
providedtoanLLMtogeneratecandidatequeries. Thesecandidatequeriesthenundergoafixing
loop,andfinally,allcandidatesarecomparedinapairwisewayusingthetrainedselectionagentto
pickthecorrectanswer. Thefollowingsectionsdelveintothedetailsofeachcomponent.
2

## Page 3

PublishedasaconferencepaperatICLR2025
Figure1: OverviewoftheproposedCHASE-SQLframeworkforText-to-SQL,withvalueretrievalandusing
a selection agent for improve picking of the answers among the generated candidates along with a fixer to
providefeedbackforrefinementoftheoutputs.
2.2 VALUERETRIEVAL
Databasesmightcontainveryhighnumberofrows,withoftenonlyafewbeingrelevanttoaquery.
RetrievingrelevantvaluesiscrucialastheycanbeusedinvariousSQLclauseslike‘WHERE’and
‘HAVING’.Similartotheapproachin(Talaeietal.,2024),webeginbyextractingkeywordsfrom
thegivenquestionusinganLLMpromptedwithfew-shotexamples. Foreachkeyword,weemploy
locality-sensitivehashing(LSH)(Dataretal.,2004)toretrievethemostsyntactically-similarwords,
andre-rankthembasedonembedding-basedsimilarityandeditdistance. Thisapproachisrobustto
typosinthequestionandconsiderskeywordsemanticsduringretrieval.
2.3 MULTI-PATHCANDIDATEGENERATION
AsshowninTable1,relyingsolelyonconsistencyamongresponsescanleadtosub-optimalperfor-
mance. Therefore,weprioritizediversityingenerationofmultipleresponsecandidatestoincrease
thelikelihoodofgeneratingatleastonecorrectanswer. Amongthediverseresponsesgeneratedby
thecandidategenerators, weselectoneasthefinalresponseusingaselectionagentthatcompares
candidatespairwise. Togeneratediverseresponses, weincreasethenexttokensamplingtempera-
ture,andalsoshuffletheorderofcolumnsandtablesintheprompt.
Chain-of-Thought(CoT)prompting(Weietal.,2022)hasbeenproposedtoenhanceLLMs’reason-
ing abilities by conditioning their final responses on a step-by-step chain of reasoning. Most CoT
prompting approaches rely on few-shot examples in the prompt to guide LLMs on thinking step-
by-step,followingtheformatM = (q,r,s),whereq istheexamplequestion,r isthereasoning
i i i i i
path,ands isthegroundtruthSQLqueryforq. Weemploytwodistinctreasoningmethodsandan
i i
onlinesyntheticexamplegenerationapproach. AsshowninFig. 3a,differentgeneratorscanyield
differentoutputs,indicatingtheireffectivenessforspecificquestionsanddatabases.
DivideandConquerCoT: Divide-and-conquerperspectivebringsbreakingdowncomplexprob-
lems into smaller sub-problems, solving each individually, and then combining the solutions to
obtainthefinalanswer. Alongtheselines,weproposeaCoTpromptingapproachthatfirstdecom-
poses the given question into smaller sub-problems using pseudo-SQL queries. In the ’conquer’
step,thesolutionstothesesub-problemsareaggregatedtoconstructthefinalanswer.Finally,anop-
timizationstepisappliedtotheconstructedquerytoremoveredundantclausesandconditions. This
approachisparticularlypowerfulhandlingcomplexscenariosthatinvolvenestedqueries,e.g. intri-
cateWHEREorHAVINGconditions,andqueriesrequiringadvancedmathematicaloperations. In
AppendixFig. 18,weexemplifyaquestionanditscorrespondingSQLquerythatwassuccessfully
solvedusingthisgenerator,ascenariotheothermethodsconsideredinthispapercouldnotaddress
due to the query’s complex conditions and SQL clauses. For a more detailed view of the divide-
and-conquer prompt, please see Appendix Fig. 17. Additionally, Alg. 1 outlines the step-by-step
processofthisstrategytogeneratethefinalSQLoutputusingasingleLLMcall.
Query Plan CoT: A query (execution) plan is a sequence of steps that the database engine fol-
lowstoaccessormodifythedatadescribedbyaSQLcommand. WhenaSQLqueryisexecuted,
thedatabasemanagementsystems’queryoptimizerstranslatetheSQLtextintoaqueryplanthatthe
databaseenginecanexecute. Thisplanoutlineshowtablesareaccessed,howtheyarejoined,and
3

## Page 4

PublishedasaconferencepaperatICLR2025
Algorithm1DivideandConquerChain-of-Thought(CoT)StrategyforText-to-SQL.
Require: Setofhuman-annotatedfew-shotexamplesM,userquestionQu,targetdatabaseDassociated
withthequestion,andalargelanguagemodel(LLM)θ.
Divide:
1: Sq←θ(M,D,Qu)//DecomposetheoriginalquestionQuintoasetofsub-questionsSq
2: Ssql←∅//InitializeanemptysetSsqltostorepartialSQLqueriesforeachsub-question
Conquer:
3: foreachsub-questionqiinSqdo
4: //GenerateapartialSQLqueryforeachsub-questionqi
5: Ssql←Ssql∪{θ(M,D,Qu,q1,...,qi,sql1,...,sqli−1)}
6: endfor
Assemble:
7: Sf←θ(M,D,Qu,Sq,Ssql)//AssemblethefinalSQLquerySffromallsub-queriesinSsql
8: returnSf
the specific operations performed on the data (see Appendix Fig. 20 as an example). Inspired by
thestep-by-stepprocessthatdatabaseenginesusetoexecuteSQLqueries,weproposeareasoning
strategy to construct the final SQL output. Query plans for any given SQL query can be obtained
using the “EXPLAIN” command, which provides a detailed breakdown of execution steps. How-
ever,thisoutputisoftenpresentedinaformatthatisdifficulttointerpretbyLLMs(e.g. inSQLite).
Toaddressthis,weconverttheoutputof“EXPLAIN”commandintoahuman-readabletextformat
thatalignsmorecloselywiththepretrainingdataofLLMs. Thehuman-readableversionofquery
plans consists of three key steps: (1) identifying and locating the relevant tables for the question,
(2)performingoperationssuchascounting,filtering,ormatchingbetweentables,and(3)delivering
thefinalresultbyselectingtheappropriatecolumnstoreturn. Thisreasoningmethodcomplements
the divide-and-conquer CoT strategy. While the divide-and-conquer approach is better suited for
decomposingcomplexquestions,thequeryplanapproachexcelswhenquestionsrequiremorerea-
soning over the relationships between different parts of the question and the database schema. It
systematicallyexplainswhichtablestoscan,howtomatchcolumns,andhowtoapplyfilters. Ap-
pendix Fig. 21 shows an example of a question that was answered correctly only by this method.
AppendixFig. 19providesthepromptusedforthisreasoningstrategy.
OnlineSyntheticExampleGeneration: Usingasetofhuman-annotateddemonstrationsforfew-
shot in-context learning has shown promising results on various related tasks (Pourreza & Rafiei,
2024a).Besidesusingafewselectdemonstrationshelpingwithspecifyingthetaskandillustratethe
step-by-stepprocessderivingtheoutput,questionandSQLexamplepairsarealsousedforfew-shot
in-contextlearningfortext-to-SQL(Liuetal.,2022;Nanetal.,2023). Whilepriorworksfocused
onselectingafewhandfulofrelevantexamplesfromexistingexamplepools(e.g.,trainingdataset),
wesynthesizemanyexamplepairsusingdifferentschemaelementsandSQLfeaturesperincoming
question. Unlike prior few-shot in-context learning approaches, we generate many more than just
a few (3-5) examples (Pourreza & Rafiei, 2024a; Li et al., 2024b), as we observe that many-shot
learningconsistentlyoutperformsfew-shotlearning(Agarwaletal.,2024).
Algorithm2OnlineSyntheticexamplegenerationstrategyforText-to-SQL.
Require: UserquestionQu,additionaluserhintHu,targetdatabaseDandfilteredrelevanttablecolumns
tassociatedwiththequestion,LLMθ,guidelinesRf forgeneratingexamplesbySQLfeatures,guide-
linesRtforgeneratingexampleswithfilteredschema,andthenumbersofexamplestogeneratenf,nt
respectively
1: P ←∅//{(qi,si)|qi,si∈Σ∗},whereqiisinputquestion,siisoutputSQLforthei-thexample
2: P ←P∪{θ(D,Rf,nf)}//GeneratenexampleswithentiredatabasebycommonSQLfeatures
3: P ←P∪{θ(t,Rt,nt)}//Generateexampleswithfilteredcolumnstohighlightcorrectschemausage
4: returnP
Algorithm 2 outlines the online synthetic example generation approach with two LLM generation
steps. The first step focuses on generating illustrative examples with common SQL features de-
scribedintheguidelineR . TheSQLfeaturesincludeequalityandnon-equalitypredicates,single
f
tableandmulti-tableJOIN,nestedJOIN,ORDERBYandLIMIT,GROUPBYandHAVING,var-
iousaggregationfunctions. ThesearewidelyapplicableSQLclausesandfunctions–thegenerated
exampleSQLqueries,incorporatingthesefeatures,followtheBIRDSQLfeaturedistribution(Ap-
pendixFig25a).Thesecondstepfocusesongeneratingexampleshighlightingcorrectinterpretation
oftheunderlyingdataschema–themodelθisaskedtogenerateexamplesusingt (columnselec-
i
4

## Page 5

PublishedasaconferencepaperatICLR2025
tionusinganapproachsimilarto(Talaeietal.,2024))andthataresimilartotheexamplesoutlined
inR . AppendixA.13providesthepromptsusedfortheexamplegeneration).
t
While a relevant example (e.g. showing a nested JOIN query with multiple tables) can be helpful
for questions that require complex JOIN queries, it might also mislead the LLM for overuse (e.g.
whenasimplesingletablequeryissufficient). Thisandtheinherentambiguityofnaturallanguage
query q , for which we draw the examples by relevance, make the example selection challenging.
i
Thus,wegenerateandinjecttheexamplestothepromptonlineperq . WeasktheLLMtogenerate
i
manyinput-outputpairsforin-contextlearning. Thefinalsetofsyntheticexamplesforq contains
i
examplesgeneratedwithbothR andR . ThisensuresthattheexamplesetisdiversebothinSQL
f t
features/clauses and the choice of relevant tables/columns used. The diversity of the example set
isdesirabletoavoidover-fittingtheoutputtocertainpatterns(e.g.,themodelalwayswritesaSQL
with JOIN if shown mostly JOIN examples). Mixing various examples for various SQL features
and database tables with and without column filtering is observed to result in better generation
qualityoverall(seeAppendixTable8). Thegeneratedsyntheticexamplescanguidethemodelfor
more accurate text-to-SQL generation. In Appendix A.13, Table 9, we discuss how our synthetic
example generation performs compared to selecting examples from often limited examples pools
(e.g.,trainingdatasetandcross-domaindataaugmentation(Lietal.,2024b)).
2.4 QUERYFIXER
In some cases, LLMs might generate queries that are syntactically incorrect. These queries are
clear candidates for correction, as they fail to provide the correct answers. To address this, we
applyanLLM-basedqueryfixerthatleveragestheself-reflection(Shinnetal.,2024)method. The
fixerreflectsonthepreviouslygeneratedquery,usingfeedbacksuchassyntaxerrordetailsorempty
resultsetstoguidethecorrectionprocess.Wecontinuethisiterativefixingapproachuptoaspecified
numberofattempts,β (settothreeinthispaper). AppendixFig. 22demonstratesthepromptused
forthisqueryfixingstep. Additionally,AppendixsectionA.4providesadetailedalgorithmofthe
queryfixingstep.
2.5 SELECTIONAGENT
WiththreedifferentmethodsforgeneratingSQLqueries,wecangenerateasetofcandidatequeries
for any given question. The key challenge in this step is selecting the correct SQL query from
thispoolofcandidates. Anaiveapproachwouldbetomeasureconsistencyamongthecandidates
byexecutingthem,groupingthembasedontheirexecutionresults,andselectingaqueryfromthe
largestgroupasthemostlikelycorrectanswer.However,thiswouldassumethatthemostconsistent
answer is always the best one, which is not always the case. Instead, we propose a more refined
pickingstrategy,Algorithm3,thatreliesonaselectionagent.GivenasetofcandidatesSQLqueries
C = {c ,c ,...,c }, the final responses are selected by finding the candidate that has the highest
1 2 n
scoreassignedbytheselectionmodel. Thismodelθ cantakekcandidatesandrankthembasedon
p
howaccuratelyeachofthemanswersthegivenquestion. Concretely,weformulatetheselectionof
thefinalresponseas:
 
(n)
(cid:88)k
c =argmax θ (c ,...,c |Q ,H ,D), (1)
f
c∈C
 p i1 ik u u 
i=1
whereQ referstotheuser’squestion, H istheprovidedhint, andD isthetargetdatabasefrom
u u
which the question is being asked. In Eq. 1, we pass k candidates to the selection model to be
ranked, with k being between 1 and n. In the extreme case of k = 1, the model is unable to
makecomparisonsbetweencandidates,whichcomplicatestheevaluationprocessforthemodel. As
k increases, comparing more candidates makes the process more challenging for the model, as it
needstoconsiderdifferentaspectssimultaneously. Consequently, wesetk = 2andtrainamodel
withaclassificationobjectivetocompareonlytwocandidatesatatime.
Having a set of high-quality and diverse candidates, the most straightforward solution is to em-
ploy off-the-shelf LLMs to make pairwise selections. However, experiments with Gemini-1.5-pro
showedthatusingtheLLMwithoutfine-tuningresultedinonly58.01%binaryclassificationaccu-
racy.Thisisprimarilyduetothecandidatesbeingverysimilartooneanother,requiringafine-tuned
5

## Page 6

PublishedasaconferencepaperatICLR2025
model to learn the nuances and make more accurate decisions. To train the selection agent, we
first generate candidate SQL queries on the training set (of Text-to-SQL benchmarks), and group
them into clusters based on their execution results. For cases where at least one cluster contains
correctqueriesandotherscontainsincorrectones,wecreatetrainingexamplesintheformoftuples
(Q ,C ,C ,D ,y ), where Q is the user’s question, C and C are the two candidate queries
u i j ij ij u i j
beingcompared,D isthedatabaseschemausedbybothcandidates(Usingtheunionofcandidate
ij
schemasisimportantasitreducescostandeliminatesunnecessaryinformationduringcomparison.),
andy ∈0,1isthelabelindicatingwhetherC orC isthecorrectquery. Toavoidorderbiasdur-
ij i j
ingtraining,werandomlyshuffletheorderofcorrectandincorrectqueriesineachpair. Sincethe
numberofcaseswithbothcorrectandincorrectcandidatesislimited,forinstanceswherenocorrect
candidateexists,weincludethegroundtruthSQLqueryinthepromptasahinttoguidethemodel
ingeneratingcorrectcandidates.
Algorithm3PickingthefinalSQLqueryfromapoolofcandidates.
Require: SetofcandidateSQLqueriesC={c1,c2,...,cn},userquestionQu,hintHu,targetdatabaseD,
andaselectionmodelθp,er(ci,D)astheexecutionresultofcionD
1: ri←0forallci∈C//Initializethescoreriforeachcandidatequerytozero
2: foreachdistinctpair(ci,cj)wherei(cid:54)=jdo
3: ifer(ci,D)=er(cj,D)then
4: w←i//ciisthewinneriftheexecutionresultsmatch
5: else
6: Si,j←schemaunion(ci,cj,D)//Constructunionofschemasusedinciandcj
7: w←θp(Si,j,Qu,Hu,ci,cj)w∈{i,j}//Usebinaryclassifierθptoselectthewinner,w∈{i,j}
8: endif
9: rw←rw+1//Increasethescoreofthewinnercwby1
10: endfor
11: cf←argmaxci∈Cri//SelectthecandidatewiththehighestscoreasthefinalSQLquerycf
12: returncf
In the pseudo-code for Algorithm 3, we begin by initializing a score of zero for each candidate
query. Then, for every distinct pair of queries (c ,c ), we compare both (c ,c ) and (c ,c ) to
i j i j j i
mitigate any order bias, ensuring that both candidates in a pair are fairly evaluated (ignoring the
bothsidecomparisonwillreducethefinalperformancebyroughly2%). Ifbothqueriesproducethe
sameexecutionresultonthedatabase,wemarkoneasthewinnerandincrementitsscore,asthese
resultssuggestconsistency. Iftheexecutionresultsdiffer,wegenerateaunionoftheschemaused
bybothqueriesandusethebinaryclassifiertodeterminewhichqueryismorelikelytobecorrect.
Theclassifiertakesintoaccountthequestion,thetwocandidatequeries,andthecombinedschema
to make its decision. The winner’s score is then updated accordingly. After all comparisons, the
candidate with the highest score is selected as the final query. In the rare case of a tie in the final
scores,webreakthetiebyselectingoneofthecandidatesarbitrarily.
3 EXPERIMENTS
DatasetsandModels WeevaluatetheperformanceoftheproposedCHASE-SQLframeworkon
twowidely-recognizedcross-domaindatasets: BIRD(Lietal.,2024c)andSpider(Yuetal.,2018).
BIRD contains over 12,751 unique question-SQL pairs from 95 large databases, spanning more
than37professionaldomains,withdatabasesdesignedtoresemblereal-worldscenarios,featuring
messydatarowsandcomplexschemas. Spiderconsistsof10,181questionsand5,693uniquecom-
plex SQL queries across 200 databases, covering 138 domains. The Spider dataset is divided into
non-overlapping training, development, and test sets similar to BIRD. For both, we use execution
accuracy(EX),theofficialmetricfortheirrespectiveleaderboard,astheprimaryevaluationmetric
to compare methods. Details of the models and their hyperparameters are provided in Appendix
sectionA.3.
BIRDresults Wepresenttheend-to-endText-to-SQLperformanceoftheproposedCHASE-SQL
frameworkusingClaude-3.5-sonnet,Gemini1.5pro,andMistralLargemodelsontheBIRDdevel-
opment set, and Gemini 1.5 pro on the BIRD test set. We compare with both published methods
(either with an available codebase and/or paper) and undisclosed methods. For a fair comparison
withGemini1.5pro,allLLMcallsintheClaude-3.5-sonnetsetting,exceptfortheselectionmodel,
are made using Claude-3.5-sonnet (previously-trained selection model is reused). To evaluate the
6

## Page 7

PublishedasaconferencepaperatICLR2025
performanceoffullyopen-sourcemodels,weusedafine-tunedQwen2.5-codermodel(Team,2024)
astheselectionmodelfortheMistralLargemodel.AsshowninTable2,CHASE-SQLwithGemini
1.5 pro achieves 73.01% accuracy on the BIRD development set and 73.0% on the BIRD holdout
testset,outperformingallpreviousworksandsettinganewstate-of-the-artperformance.
Table 2: Performance Comparison of different Text-Table 3: Performance Comparison of different Text-
to-SQLmethodsonBIRDbenchmark.
to-SQLmethodsonSpidertestset.
Method EX(Dev) EX(Test)
Method EX TrainingwithSpider
Published
MCS-SQL+GPT-4
CHASE-SQL+Gemini1.5(Ours) 73.01 73.0 (Leeetal.,2024) 89.6 (cid:88)
CHASE-SQL+Claude3.5Sonnet(Ours) 69.53 – CHASE-SQL+Gemini1.5(Ours) 87.6 (cid:55)
CHASE-SQL+MistralLarge(Ours) 70.33 – CHESS
Distillery+GPT-4o (Talaeietal.,2024) 87.2 (cid:55)
(Maamarietal.,2024) 67.21 71.83 DAIL-SQL+GPT-4
CHESS (Gaoetal.,2023) 86.6 (cid:88)
(Talaeietal.,2024) 65.00 66.69 DIN-SQL+GPT-4
MCS-SQL+GPT-4 (Pourreza&Rafiei,2024a) 85.3 (cid:88)
(Leeetal.,2024) 63.36 65.45 C3+ChatGPT
SuperSQL (Dongetal.,2023) 82.3 (cid:88)
(Lietal.,2024a) 58.5 62.66 RESDSQL3B
Undisclosed (Lietal.,2023a) 79.9 (cid:88)
DIN-SQL+CodeX
InsightsAI 72.16 70.26 (Pourreza&Rafiei,2024a) 78.2 (cid:88)
AskData+GPT-4o 72.03 72.39
T5-3B+NatSQL
OpenSearch-v2+GPT-4o 69.3 72.28 (Raietal.,2023) 78.0 (cid:88)
PURPLE-RED+GPT-4o 68.12 70.21
Graphix-3B+PICARD
Arcwise+GPT-4o 67.99 66.21 (Lietal.,2023b) 77.6 (cid:88)
ExSL+granite-34b-code 67.47 67.76
Spider results We assess the generalizability of the proposed CHASE-SQL by evaluating it in
an end-to-end way on the Spider test set without modifying the few-shot samples in the prompts
ortraininganewselectionmodel,i.e. withoutusinganddatafromthetargetdistribution. Thisap-
proachallowsustotesttheperformanceofCHASE-SQLondifferentunseenqueryanddatabasedis-
tributionscomparedtothedatafromtrainingdistributions. Table3demonstratesthatCHASE-SQL
achieves an execution accuracy of 87.6% on the Spider test set, placing it second among methods
thathaveundergonespecifictrainingorpromptoptimizationfortheSpiderdataset. Thishighlights
thestronggeneralizabilityofCHASE-SQLanditspotentialforgeneratinghighqualityText-to-SQL
forunseensamplescomingfromverydifferentdistributionsanduniquechallenges.
3.1 GENERATORANDSELECTIONPERFORMANCE
Generator + Fixer: To reveal performance
of generators, we conducted an ablation study Table 4: Ablationstudiesonsinglecandidategenera-
to evaluate the performance of each candidate tionperformanceofthecandidategeneratorscompared
generation method before and after applying withoriginalBIRDprompt+zero-shotCoTwithGem-
the query fixer using two models of Gemini- ini1.5proandMistralLargeontheBIRDdevset.
1.5-pro and Mistral Large (AI, 2024). We
comparetheperformanceoftheproposedgen- Gemini1.5pro MistralLarge
erators in producing a single candidate query Method EX(%) ∆(%) EX(%) ∆(%)
against the original BIRD prompt (Li et al., Baseline 57.75 - 54.88 -
QPCoT 63.62 +5.87 59.64 4.76
2024c),augmentedwithzero-shotCoTreason- DCCoT 63.92 +6.17 58.99 4.11
ing (Kojima et al., 2022), which serves as the OSICL 67.09 +9.34 56.32 1.44
BaselinewQueryFixer 61.58 +3.83 60.03 5.15
baseline for assessing the quality of prompts. QPCoTwQueryFixer 65.51 +7.76 62.64 7.76
Theresults,showninTable4,indicatethatthe DCCoTwQueryFixer 65.77 +8.02 63.75 8.87
OSICLwQueryFixer 68.02 +10.27 61.47 6.59
proposed methods significantly improve SQL
generationperformance,comparedtothenaive
baseline,towardsthegoalofproducinghigh-qualitycandidateswhilemaintainingdiversity.Among
thecandidategenerators,theonlinesyntheticdatagenerationapproachproducedanimpressiveper-
formanceof68.02%withGemini-1.5-promodel,demonstratingitseffectivenessinleveragingtest-
time compute to improve LLM performance by generating high-quality synthetic examples. Fur-
thermore,thequeryfixerprovedcrucial,enhancingthequalityofthecandidatepoolandincreasing
performancebynearly2%acrossallcandidategenerators.
7

## Page 8

PublishedasaconferencepaperatICLR2025
Selection: We conducted an analysis on the binary selection accuracy of the selection agent for
cases where, in a pairwise comparison, one candidate is correct and the other is incorrect. We
excludecaseswherebothcandidatesareeithercorrectorincorrect,astheselectionwouldnotaffect
theoutcomesincebothcandidateshavethesamelabel.WecomparetheperformanceofClaude-3.5-
sonnetandGemini-1.5-pro(bothout-of-the-boxwithoutfine-tuning)withtwofine-tunedmodels:1)
Gemma29Band2)Gemini-1.5-flash. AsshowninTable5,bothfine-tunedmodelsachievehigher
accuracy than the untuned counterparts, demonstrating the importance of fine-tuning to teach the
modelaboutthespecificpreferences.
Candidate Generation Analysis: We analyze the
performanceofeachcandidategeneratormethodindi- Table5: Evaluatingthebinaryselectionaccu-
vidually. Tobetterunderstandtheperformancepoten- racyofthedifferentselectionmodels.
tial when effectively selecting the correct SQL query
fromthecandidatepool,wegeneratesevencandidate
SelectionModel BinaryAcc.(%)
SQL queries from each generator method (21 candi-
datesintotal)forallsamplesintheBIRDdevelopment Claude-3.5-sonnet 60.21
set. Wedeterminethisnumberofcandidatesbasedon Gemini-1.5-pro 63.98
TunedGemma29B 64.28
theobservationthatincreasingthecandidatepoolbe-
TunedGemini-1.5-flash 71.01
yond20didnotyieldsignificantimprovements,asil-
lustratedinFig. 2d. Byassumingaccesstoanoracle
selectionmodelthatalwaysselectsthecorrectSQLqueryfromthesevencandidates,wecalculate
the upper-bound performance achievable for each generator. Conversely, by assuming an adver-
sarial selection model that always selects the wrong SQL query, we determine the lower-bound
performance. Fig. 2illustratestheupper-boundandlower-boundperformanceforallthreemethods
together with the performance of our selection agent. As shown, the upper-bound performance of
the two different CoT methods is generally higher than that of the synthetic example generation
methodfordifferentnumberofcandidates. However,theirlower-boundperformanceisalsolower
than the synthetic method. Lower-bound accuracy reflects cases where all candidates are correct,
reducing the noise in the selection process since it doesn’t matter which candidate is chosen, so a
higherlower-boundispreferred. Thisisevidentintheselectionagent’sperformance,whereadrop
inthelowerboundleadstodiminishingreturnsfromincreasingtheupperbound,causingtheselec-
tion agent’s performance to plateau. Additionally, the upper-bound performance of combining all
three methods reaches 82.79%, highlighting the significant room for improvement through better
candidatepickingmethods. ThisdemonstratesthattheLLM’sparametricknowledgealreadycon-
tainstheinformationneededtosolvemostquestions,highlightingtheneedforensembleapproaches
toeffectivelyextractandutilizethisknowledge.
Additionally, we evaluate the upper-bound performance by combining all candidates from three
candidategenerationmethodsacrossthesimple,moderate,andchallengingdifficultylevelsforthe
BIRD development set. These difficulty categories are assigned by human experts during the cre-
ationoftheBIRDdevelopmentset. Fig. 2dshowsthat,asexpected,theupper-boundperformance
increases with the number of candidates across all difficulty levels. However, for the challenging
andmoderateclasses,theimprovementplateausearlierthaninthesimpleclass,suggestingthatgen-
eratingmoresamplesdoesnotfurtherimprovetheupper-boundperformanceforthesetwodifficulty
levels.
Fig. 2 presents a Venn diagram showcasing the performance of three generation methods: Query
Plan, Divide and Conquer, and with Synthetic Examples. The numbers within the intersecting re-
gionsrepresenttheinstanceswheremultiplemethodsgeneratedatleastonecorrectcandidate. This
diagramvisuallyhighlightstheuniquecontributionsofeachmethod,whichindicatesthenecessity
of using all three generators. Additionally, in Fig. 3b, we compare the number of correct queries
generatedbyeachSQLgenerationmethodthatarenotcorrectbytheothergenerators. Thedivide-
and-conquerapproachoutperformstheothersonchallengingquestions,whilethequeryplanmethod
excelsonmoderatelydifficultqueries. Tofurtheranalyzetheperformanceofthegeneratorsacross
different domains and varying numbers of columns and tables, we compare the number of correct
queriesgeneratedforeachdatabase,asshowninAppendixFig.5.Asillustrated,bothCoTmethods
generallyperformsimilarlyacrossdatabases,whiletheonlinesyntheticexamplegenerationmethod
significantlyincreasesdiversity,resultinginmorecorrectanswersoverallacrossdifferentdatabases.
8

## Page 9

PublishedasaconferencepaperatICLR2025
(a) Upper-bound and lower-bound Accuracy for (b) Upper-bound and lower-bound Accuracy for
DivideandConquerCoT OnlineSyntheticExample
(d) Upper-bound performance of all three can-
(c) Upper-bound and lower-bound performance didate generators across different difficulty cate-
forQueryPlanCoT. gories.
Figure2:Comparisonoftheupper-andlower-boundperformanceofdifferentcandidategenerators.
Query Plan Synthetic Example
33
35 30
1045
72 23
38
Divide and Conquer
Unsolved Questions: 258
(a)Venndiagramillustratingthenumberof
instances for which each method: Query
Plan,SyntheticExample,DivideandCon-
quer, produces at least one correct candi-
date. Theoverlapregionsrepresentmulti- (b) Number of correct queries across different complexity
plemethodsgeneratingcorrectcandidates. levelsthatwereansweredbyeachmethod.
Figure3: ComparisonofSQLgenerationmethods: Venndiagramshowinguniqueandoverlapping
correctanswers(left)andtheperformanceacrossdifferentcomplexitylevels(right).
Selection Agent Analysis: We evaluate the query-picking performance by comparing the Text-
to-SQLexecutionaccuracyoftheselectionagentwiththeself-consistencymethod(usingmajority
voting)Wangetal.(2022),anoraclemodel(upperbound),andanadversarialmodel(lowerbound).
To conduct the evaluation, we generate 10 samples from each candidate generation method using
twodifferentsamplingtemperatures:0.5and1.8.Theresults,showninTable6,demonstratethatthe
selectionagentsignificantlyoutperformstheself-consistencymethodwithalargemargin,roughly
6%. Asexpected, increasingthesamplingtemperatureraisestheupperboundbutalsolowersthe
lower bound. This effect is more pronounced for the synthetic data generation method compared
tothetwoCoTmethods,mainlybecauseLLMsgeneratereasoningstepsbeforeproducingthefinal
SQL query, which helps mitigate the randomness introduced by high-temperature sampling. The
performance with self-consistency method generally decreases as temperature increases, since the
9

## Page 10

PublishedasaconferencepaperatICLR2025
majorityclusterbecomessmallerwithmorerandomqueries. However,theproposedtrainedselec-
tionagentislessaffectedbytemperaturescalingand,intwocases,evenimproveditsperformance
withamorediversepoolofsamples.
Table6: Performancecomparisonofdifferentpickingmethodsonthecandidatesgeneratedbythecandidate
generatorsonBIRDdevelopmentsetwithtwodifferenttemperatures.QPreferstoqueryplanCOT,DCrefers
todivideandconquerCOT,andOSistheonlinesyntheticexamplegenerationmethod.
PickingMethod QP(T=0.5) QP(T=1.8) DC(T=0.5) DC(T=1.8) OS(T=0.5) OS(T=1.8)
LowerBound 50.46 48.63 51.37 47.39 60.43 50.98
UpperBound 78.55 80.44 78.42 79.34 74.77 79.66
Self-consistency 65.78 65.51 66.43 64.41 67.34 66.88
OurSelectionAgent 71.7 71.73 71.31 70.53 70.4 71.38
3.2 ABLATIONSTUDIES
In the previous sections, we evaluate
the importance of the selection agent Table7: AblationstudiesontheperformanceofCHASE-SQL
and each candidate generation method. afterremovingthequeryfixer,LSHforvalueretrieval,andrea-
Next,wefocusontheanalysisofthere- soningstrategies,i.e.,QP,OS,andDC.
maining components of CHASE-SQL:
LSHforvalueretrieval,thequeryfixer, Method ExecutionAccuracy(%) ∆(%)
and three reasoning strategies (QP, OS, CHASE-SQLAll 73.01 -
and DC). Table 7 shows the perfor- CHASE-SQLwself-consistency 68.84 -4.17
CHASE-SQLwrankeragent 65.51 -7.5
manceofCHASE-SQLwithouteachof CHASE-SQLw/oLSH 70.09 -2.92
these steps, highlighting their signifi- CHASE-SQLw/oQueryFixer 69.23 -3.78
CHASE-SQLw/oQP 72.36 -0.65
cance in achieving higher-quality per- CHASE-SQLw/oOS 72.16 -0.85
formance. The results demonstrate the CHASE-SQLw/oDC 71.77 -1.24
contribution of each component, where
removing LSH, the query fixer, or any of the candidate generators leads to a reduction in execu-
tion accuracy, further validating the importance of these components of CHASE-SQL. Moreover,
thetablecomparestheperformanceofourbinaryselectionagentwithtwootherselectionmethods:
self-consistency (Wang et al., 2022) and a ranker agent. The ranker agent receives all candidates
generatedbyourthreecandidategeneratorsinasingleprompt,comparesthem,andproducearank-
ing for each. For the ranker agent, we select the query with the lowest rank as the best answer.
The binary selection agent significantly outperforms both the self-consistency and ranker agents,
demonstratingtheeffectivenessoftheproposedmethod.
4 CONCLUSION
Weintroduceanovelagenticframework,CHASE-SQL,toleveragetest-timecomputeforgenerat-
ingdiverse,high-qualitySQLqueriesandaccuratelyselectingthecorrectone. Weproposemultiple
chain-of-thoughtpromptingmethodsandanonlinesyntheticexamplegenerationtechnique, along
withaqueryselectionmechanismthatscorescandidatesbasedonpairwisecomparisons.Ourframe-
work, CHASE-SQL, sets a new state-of-the-art in the notable public Text-to-SQL leaderboard (at
thetimeofthesubmission),demonstratingtheeffectivenessoftest-timecomputationforbothgen-
eratingdiversequeriesandselectingthemostaccurateresponse. CHASE-SQLaddresseskeyissues
likequerydiversityandselectionoptimization,pavingthewayforfurtherimprovementsincomplex
reasoningtasksencounteredatreal-worldText-to-SQLchallenges.
REFERENCES
RishabhAgarwal,AviSingh,LeiMZhang,BerndBohnet,LuisRosias,StephanieC.Y.Chan,Biao
Zhang, AleksandraFaust, andHugoLarochelle. Many-shotin-contextlearning. InICML2024
Workshop on In-Context Learning, 2024. URL https://openreview.net/forum?id=
goi7DFHlqS.
Mistral AI. Mistral large 2407. https://mistral.ai/news/mistral-large-2407/,
2024. Accessed: 2024-11-16.
10

## Page 11

PublishedasaconferencepaperatICLR2025
Ion Androutsopoulos, Graeme D Ritchie, and Peter Thanisch. Natural language interfaces to
databases–anintroduction. Naturallanguageengineering,1(1):29–81,1995.
RuichuCai,JinjieYuan,BoyanXu,andZhifengHao. Sadga: Structure-awaredualgraphaggrega-
tionnetworkfortext-to-sql. AdvancesinNeuralInformationProcessingSystems,34:7664–7676,
2021.
RuishengCao,LuChen,ZhiChen,YanbinZhao,SuZhu,andKaiYu. Lgesql: linegraphenhanced
text-to-sql model with mixed local and non-local relations. arXiv preprint arXiv:2106.01093,
2021.
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared
Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. Evaluating large
languagemodelstrainedoncode. arXivpreprintarXiv:2107.03374,2021.
XinyunChen,MaxwellLin,NathanaelScha¨rli,andDennyZhou. Teachinglargelanguagemodels
toself-debug. arXivpreprintarXiv:2304.05128,2023.
DongHyunChoi,MyeongCheolShin,EungGyunKim,andDongRyeolShin.Ryansql:Recursively
applyingsketch-basedslotfillingsforcomplextext-to-sqlincross-domaindatabases. Computa-
tionalLinguistics,47(2):309–332,2021.
Mayur Datar, Nicole Immorlica, Piotr Indyk, and Vahab S Mirrokni. Locality-sensitive hashing
scheme based on p-stable distributions. In Proceedings of the twentieth annual symposium on
Computationalgeometry,pp.253–262,2004.
XuemeiDong,ChaoZhang,YuhangGe,YurenMao,YunjunGao,JinshuLin,DongfangLou,etal.
C3: Zero-shottext-to-sqlwithchatgpt. arXivpreprintarXiv:2307.07306,2023.
Dawei Gao, Haibin Wang, Yaliang Li, Xiuyu Sun, Yichen Qian, Bolin Ding, and Jingren Zhou.
Text-to-sql empowered by large language models: A benchmark evaluation. arXiv preprint
arXiv:2308.15363,2023.
Jonathan Herzig, Paweł Krzysztof Nowak, Thomas Mu¨ller, Francesco Piccinno, and Julian Mar-
tin Eisenschlos. Tapas: Weakly supervised table parsing via pre-training. arXiv preprint
arXiv:2004.02349,2020.
Vagelis Hristidis, Yannis Papakonstantinou, and Luis Gravano. Efficient ir-style keyword search
overrelationaldatabases. InProceedings2003VLDBConference,pp.850–861.Elsevier,2003.
WonseokHwang,JinyeongYim,SeunghyunPark,andMinjoonSeo. Acomprehensiveexploration
onwikisqlwithtable-awarewordcontextualization. arXivpreprintarXiv:1902.01069,2019.
GeorgeKatsogiannis-MeimarakisandGeorgiaKoutrika. Asurveyondeeplearningapproachesfor
text-to-sql. TheVLDBJournal,32(4):905–936,2023.
Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large
language models are zero-shot reasoners. Advances in neural information processing systems,
35:22199–22213,2022.
Dongjun Lee, Choongwon Park, Jaehyuk Kim, and Heesoo Park. Mcs-sql: Leveraging
multiple prompts and multiple-choice selection for text-to-sql generation. arXiv preprint
arXiv:2405.07467,2024.
BoyanLi,YuyuLuo,ChengliangChai,GuoliangLi,andNanTang. Thedawnofnaturallanguage
tosql: Arewefullyready? arXivpreprintarXiv:2406.01265,2024a.
FeiLiandHosagraharVJagadish. Constructinganinteractivenaturallanguageinterfaceforrela-
tionaldatabases. ProceedingsoftheVLDBEndowment,8(1):73–84,2014.
Haoyang Li, Jing Zhang, Cuiping Li, and Hong Chen. Resdsql: Decoupling schema linking and
skeletonparsingfortext-to-sql. InProceedingsoftheAAAIConferenceonArtificialIntelligence,
volume37,pp.13067–13075,2023a.
11

## Page 12

PublishedasaconferencepaperatICLR2025
Haoyang Li, Jing Zhang, Hanbing Liu, Ju Fan, Xiaokang Zhang, Jun Zhu, Renjie Wei, Hongyan
Pan, Cuiping Li, and Hong Chen. Codes: Towards building open-source language models for
text-to-sql. ProceedingsoftheACMonManagementofData,2(3):1–28,2024b.
JinyangLi,BinyuanHui,ReynoldCheng,BowenQin,ChenhaoMa,NanHuo,FeiHuang,Wenyu
Du, Luo Si, and Yongbin Li. Graphix-t5: Mixing pre-trained transformers with graph-aware
layersfortext-to-sqlparsing. arXivpreprintarXiv:2301.07507,2023b.
Jinyang Li, Binyuan Hui, Ge Qu, Jiaxi Yang, Binhua Li, Bowen Li, Bailin Wang, Bowen Qin,
Ruiying Geng, Nan Huo, et al. Can llm already serve as a database interface? a big bench for
large-scaledatabasegroundedtext-to-sqls. AdvancesinNeuralInformationProcessingSystems,
36,2024c.
Yujia Li, David Choi, JunyoungChung, Nate Kushman, Julian Schrittwieser, Re´mi Leblond, Tom
Eccles,JamesKeeling,FelixGimeno,AgustinDalLago,etal.Competition-levelcodegeneration
withalphacode. Science,378(6624):1092–1097,2022.
JiachangLiu, DinghanShen, YizheZhang, BillDolan, LawrenceCarin, andWeizhuChen. What
makes good in-context examples for GPT-3? In Eneko Agirre, Marianna Apidianaki, and Ivan
Vulic´ (eds.), Proceedings of Deep Learning Inside Out (DeeLIO 2022): The 3rd Workshop on
Knowledge Extraction and Integration for Deep Learning Architectures, pp. 100–114, Dublin,
Ireland and Online, May 2022. Association for Computational Linguistics. doi: 10.18653/v1/
2022.deelio-1.10. URLhttps://aclanthology.org/2022.deelio-1.10.
Karime Maamari, Fadhil Abubaker, Daniel Jaroslawicz, and Amine Mhedhbi. The death of
schema linking? text-to-sql in the age of well-reasoned language models. arXiv preprint
arXiv:2408.07702,2024.
LinyongNan,YilunZhao,WeijinZou,NarutatsuRi,JaesungTae,EllenZhang,ArmanCohan,and
DragomirRadev. Enhancingfew-shottext-to-sqlcapabilitiesoflargelanguagemodels: Astudy
onpromptdesignstrategies. arXivpreprintarXiv:2305.12586,2023.
AnsongNi,SriniIyer,DragomirRadev,VeselinStoyanov,Wen-tauYih,SidaWang,andXiVictoria
Lin. Lever: Learning to verify language-to-code generation with execution. In International
ConferenceonMachineLearning,pp.26106–26128.PMLR,2023.
Rube´nPe´rez-Mercado,AntonioBalderas,Andre´sMun˜oz,JuanFranciscoCabrera,ManuelPalomo-
Duarte,andJuanManuelDodero.Chatbotsql:Conversationalagenttosupportrelationaldatabase
querylanguagelearning. SoftwareX,22:101346,2023.
MohammadrezaPourrezaandDavoodRafiei. Din-sql: Decomposedin-contextlearningoftext-to-
sqlwithself-correction. AdvancesinNeuralInformationProcessingSystems,36,2024a.
Mohammadreza Pourreza and Davood Rafiei. Dts-sql: Decomposed text-to-sql with small large
languagemodels. arXivpreprintarXiv:2402.01117,2024b.
Mohammadreza Pourreza, Ruoxi Sun, Hailong Li, Lesly Miculicich, Tomas Pfister, and Sercan O
Arik. Sql-gen: Bridging the dialect gap for text-to-sql via synthetic data and model merging.
arXivpreprintarXiv:2408.12733,2024.
Abdul Quamar, Vasilis Efthymiou, Chuan Lei, and Fatma O¨zcan. Natural language interfaces to
data. Found.TrendsDatabases,11(4):319–414,2022. doi: 10.1561/1900000078. URLhttps:
//doi.org/10.1561/1900000078.
DakingRai,BailinWang,YilunZhou,andZiyuYao. Improvinggeneralizationinlanguagemodel-
based text-to-sql semantic parsing: Two simple semantic boundary-based techniques. arXiv
preprintarXiv:2305.17378,2023.
NoahShinn,FedericoCassano,AshwinGopinath,KarthikNarasimhan,andShunyuYao.Reflexion:
Languageagentswithverbalreinforcementlearning.AdvancesinNeuralInformationProcessing
Systems,36,2024.
12

## Page 13

PublishedasaconferencepaperatICLR2025
Ruoxi Sun, Sercan O¨ Arik, Alex Muzio, Lesly Miculicich, Satya Gundabathula, Pengcheng Yin,
Hanjun Dai, Hootan Nakhost, Rajarishi Sinha, Zifeng Wang, et al. Sql-palm: Improved large
languagemodeladaptationfortext-to-sql(extended). arXivpreprintarXiv:2306.00739,2023.
Shayan Talaei, Mohammadreza Pourreza, Yu-Chen Chang, Azalia Mirhoseini, and Amin Saberi.
Chess: Contextualharnessingforefficientsqlsynthesis. arXivpreprintarXiv:2405.16755,2024.
Qwen LM Team. Qwen2.5-coder. https://qwenlm.github.io/blog/qwen2.
5-coder/,2024. Accessed: 2024-11-16.
Bailin Wang, Richard Shin, Xiaodong Liu, Oleksandr Polozov, and Matthew Richardson. Rat-
sql: Relation-aware schema encoding and linking for text-to-sql parsers. arXiv preprint
arXiv:1911.04942,2019.
BingWang, ChangyuRen, JianYang, XinnianLiang, JiaqiBai, Qian-WenZhang, ZhaoYan, and
ZhoujunLi.Mac-sql:Multi-agentcollaborationfortext-to-sql.arXivpreprintarXiv:2312.11242,
2023.
XuezhiWang,JasonWei,DaleSchuurmans,QuocLe,EdChi,SharanNarang,AakankshaChowdh-
ery,andDennyZhou. Self-consistencyimproveschainofthoughtreasoninginlanguagemodels.
arXivpreprintarXiv:2203.11171,2022.
JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,FeiXia,EdChi,QuocVLe,Denny
Zhou,etal. Chain-of-thoughtpromptingelicitsreasoninginlargelanguagemodels. Advancesin
neuralinformationprocessingsystems,35:24824–24837,2022.
TianbaoXie,FanZhou,ZhoujunCheng,PengShi,LuoxuanWeng,YitaoLiu,TohJingHua,Jun-
ning Zhao, Qian Liu, Che Liu, et al. Openagents: Anopen platformfor language agentsin the
wild. arXivpreprintarXiv:2310.10634,2023.
PengchengYin,GrahamNeubig,Wen-tauYih,andSebastianRiedel. Tabert: Pretrainingforjoint
understandingoftextualandtabulardata. arXivpreprintarXiv:2005.08314,2020.
TaoYu, RuiZhang, KaiYang, MichihiroYasunaga, DongxuWang, ZifanLi, JamesMa, IreneLi,
QingningYao,ShanelleRoman,etal. Spider: Alarge-scalehuman-labeleddatasetforcomplex
andcross-domainsemanticparsingandtext-to-sqltask. arXivpreprintarXiv:1809.08887,2018.
Tao Yu, Chien-Sheng Wu, Xi Victoria Lin, Bailin Wang, Yi Chern Tan, Xinyi Yang, Dragomir
Radev,RichardSocher,andCaimingXiong. Grappa: Grammar-augmentedpre-trainingfortable
semanticparsing. arXivpreprintarXiv:2009.13845,2020.
13

## Page 14

PublishedasaconferencepaperatICLR2025
A APPENDIX
A.1 LIMITATIONSANDFUTUREWORKS
Based on the analysis presented in this paper, we demonstrate that the parametric knowledge of
recent large language models, such as Gemini-1.5-pro and Mistral Large, contains the necessary
informationtoanswermostchallengingquestionsinnotabletext-to-SQLbenchmarks,asevidenced
by their high pass@K performance. This highlights the challenge of effectively utilizing the rea-
soning ability of these models to select the best answer among the candidates. In our work, we
concluded that pairwise comparison is an effective approach to identify the best candidate. How-
ever,webelievethisperformancecouldbefurtherimprovedbyleveragingthereasoningcapabilities
of the models, either through chain-of-thought prompting or employing more sophisticated search
methods, which we leave as directions for future work. Additionally, further research is needed
toaddressthedetectionofambiguousquestionsandtoimprovethereliabilityoftext-to-SQLsys-
tems. Mostmethodologiesinthisdomainassumethatallquestionsareanswerable,whichremains
asignificantlimitationincurrenttext-to-SQLapproaches.
A.2 RELATEDWORKS
Early Text-to-SQL methods predominantly utilized sequence-to-sequence architectures, encoding
user queries and database schemas using models such as Graph Neural Networks (GNNs), Re-
current Neural Networks (RNNs), Long Short-Term Memory (LSTM) networks, and pre-trained
transformerencoders(Hwangetal.,2019;Caietal.,2021;Caoetal.,2021). Onthedecodingside,
thesesystemsemployedeitherslot-fillingorauto-regressivemodellingapproachestoconstructthe
finalSQLqueriesfromtheencodedinputs(Choietal.,2021;Wangetal.,2019). Additionally,tab-
ularlanguagemodelslikeTaBERT(Yinetal.,2020),TaPas(Herzigetal.,2020),andGrappa(Yu
etal., 2020)havebeendeveloped toencodeboth tablesandtextualdata effectively. However, the
landscapehasevolvedwiththewidespreaduseofLLMs,whichhavelargelyreplacedearliermeth-
ods with their superior performance (Katsogiannis-Meimarakis & Koutrika, 2023; Quamar et al.,
2022). Initially, efforts concentrated on optimizing prompt designs for these LLMs (Pourreza &
Rafiei,2024a;Gaoetal.,2023;Dongetal.,2023). Subsequentadvancementshaveintroducedmore
complex methodologies, including schema linking (Li et al., 2024b; Talaei et al., 2024; Pourreza
& Rafiei, 2024a;b), self-correction or self-debugging (Chen et al., 2023; Wang et al., 2023; Ta-
laei et al., 2024), and self-consistency techniques (Lee et al., 2024; Sun et al., 2023; Talaei et al.,
2024;Maamarietal.,2024),furtherenhancingtheperformancebyproposingcomplexLLM-based
pipelines.
As previously discussed, one approach to enhance Text-to-SQL performance is based on the con-
sistency of LLM responses. The self-consistency approach, as proposed by Wang et al. (2022),
involvessamplingmultipleresponsesfromanLLMandselectingthemostconsistentanswerbased
onthemajorityvote. IntheText-to-SQLcontext,thistechniqueextendstogeneratingmultipleSQL
queriesforagivenquestion,groupingthesequeriesbytheirexecutionresults,andselectingaquery
fromthelargestclusterasthemostconsistentanswer(Gaoetal.,2023;Sunetal.,2023;Talaeietal.,
2024).However,recentstudieshavepointedoutthelimitationsofthismethodinreliablyidentifying
thecorrectanswer. Inresponse,MCS-SQL(Leeetal.,2024)introducedanapproachthatutilizesan
LLMtorerankthemostconsistentanswers,movingbeyondsimplemajorityvoting. Despitethese
advancements, reliance on consistency as a filtering mechanism can inadvertently exclude correct
queriesthatarelessfrequentamonggeneratedcandidates,asacriticalbottleneck.
A.3 MODELS
All experiments are conducted using models from the Gemini and Claude, known for their ability
tohandlelongcontextualinformation(Maamarietal.,2024),whichiscrucialfortheText-to-SQL
task involving queries from large databases. For candidate generation, online synthetic example
generation, query fixing, column filtering, and keyword extraction, we reported the performance
withtwomodelsofGemini1.5ProandClaude-3.5-Sonnet. Forthequery-pickingmodel,wetraina
Gemini1.5Flashmodel(whichhasmuchlesslatencythantheGemini1.5Promodel)onadataset
of3.8KsamplesgeneratedbyrunningthecandidategeneratorsontheBIRDtrainingdataset. The
14

## Page 15

PublishedasaconferencepaperatICLR2025
Gemini 1.5 Flash model is trained for 10 epochs using a LoRA adapter with a rank of 16 using
VertexAItuningAPI.
A.4 QUERYFIXINGALGORITHM
Inthissection,wepresentthealgorithmofthequeryfixingstepofourproposeapproach.
Algorithm4Queryfixingmethod.
Require: SetofcandidateSQLqueriesC={c1,c2,...,cn},userquestionQu,hintHu,targetdatabaseD,
maxqueryfixingthresholdβ,andafixermodelθf
1: Cfixed←∅// InitializeanemptysetCfixedtostorethefixedqueries
2: foreachcandidatequeryci∈Cdo
3: Executioni←Execute(ci,D)//ExecutetheSQLqueryoverthedatabase
4: iferrorinExecutioniorExecutioni=[]then
5: forj∈{1,2,...,β}do//Tryfixinguptoβtimes
6: ci←θf(D,ci,Executioni)//Fixthequeryusingthefixermodel
7: Executioni←Execute(ci,D)//Re-executethefixedquery
8: ifnot(errorinExecutioniorExecutioni=[])then
9: Cfixed←Cfixed∪{ci}//Addthefixedquerytotheset
10: break//Exitthefixingloopifsuccessful
11: endif
12: endfor
13: else
14: Cfixed←Cfixed∪{ci}//Addthequeryasisifnofixingisneeded
15: endif
16: endfor
17: returnCfixed//Returnthesetoffixedqueries
15

## Page 16

PublishedasaconferencepaperatICLR2025
A.5 VALUERETRIEVALEXAMPLE
Inthissection, weprovideanexampleofthevalueretrievalstep. FortheGivenQuestion: “What
is the highest eligible free rate for K-12 students in the schools in Alameda County?”, from the
“california schools”Database,theclosestdatabasevaluesthatareretrievedfromtheLSHandafter
rerankingareasfollows:
Table”schools”:
”SOCType”: [”Preschool”],
”EILName”: [”Preschool”],
”School”: [
”Preschool”,
”MethodSchools”,
”AlamedaCountyCommunity”,
”AlamedaCountyOpportunity”,
”AlamedaHigh”],
”MailStreet”: [”4600StudentLane”],
”Street”: [”4600StudentLane”],
”AdmLName1”: [”Free”],
”AdmLName2”: [”Freeman”],
”MailCity”: [”Alameda”],
”City”: [”Alameda”],
”AdmFName1”: [”Kate”,”Nate”,”Bree”],
”GSserved”: [”K-12”],
”GSoffered”: [”K-12”],
”StreetAbr”: [”4600StudentLn.”],
”MailStrAbr”: [”4600StudentLn.”],
”AdmLName3”: [”Yount”],
”AdmFName3”: [”Bree”],
”County”: [”Alameda”],
”District”: [”AlamedaUnified”,”Tri-CountyROP”],
Table”frpm”:
”SchoolType”: [”Preschool”],
”SchoolName”: [
”MethodSchools”,
”AlamedaCountyCommunity”,
”AlamedaHigh”
],”CountyName”: [”Alameda”],
Table”satscores”:
”sname”: [”AlamedaHigh”],
”cname”: [”Alameda”],
”dname”: [”AlamedaCountyOfficeofEducation”]
Figure4: AnexampleofthedivideandconquerCoTmethod
A.6 PERFORMANCEBASEDONDATABASE
Inthissection,wepresentthenumberofsamplesacrossdifferentdatabaseswhereonlyoneofthe
candidate generators produces a correct result, meaning the other two generators fail to provide
a correct answer. A value of zero for any generator in this figure indicates that whenever that
generator produces a correct result, the other two generators also manage to generate at least one
correctanswer.
16

## Page 17

PublishedasaconferencepaperatICLR2025
Figure5: NumberofcorrectqueriesbyeachmethodacrossdifferentdatabasesofBIRDdevelopmentset.
A.7 ERRORANALYSIS
Figure6:Distributionofsystemperformancebasedonthefinalanswercorrectness.Thechartshows
the proportion of correct final answers, correct queries existing among candidates but not chosen
(wrongselection),nocorrectcandidatecases,andcaseswerethegoldenSQLqueryiswrong.
Fig. 6providesapiechartthatbreaksdownthesystem’sperformanceintofourcategories: correct
finalanswer(72.9%),correctexistsamongcandidatesbutnotchosen(10.4%),wronggenerationsor
nocorrectcandidate(6.7%),andwronggoldenquery(10.0%).Themajorityofresponsesarecorrect
finalanswers,butanotableportionfallsundercorrectanswersnotbeingchosenbythesystem. This
breakdownhelpsinunderstandingareaswherethesystemexcelsandwhereimprovementscanbe
targeted.
17

## Page 18

PublishedasaconferencepaperatICLR2025
100
80
60
40
20
0
California Schoo C ls ard Games Codebase Comm D u e n b it it y Card Spec E ia u l r iz o i p n e g an Footba F l i l n 2 ancial Formula 1 Student Club Superhero Thrombosis Pred T i o c x t i i c o o n logy
)%(
egatnecreP
97.7% Correct Exists Among Candidates
92.4% 90.7% Correct is Chosen by Picker
88.6%
84.3% 82.8% 82.8% 82.9% 85.8% 82.8%
79.3% 77.9%
72.8% 73.7% 75.2%
70.3% 70.8% 70.3%
67.4% 66.1%
63.9%
61.3%
Figure7: Correctnesscomparisonofthesystemacrossdifferentdatabasesintwometrics: (1)per-
centagewherethecorrectqueryexistsamongthecandidates,and(2)percentagewherethecorrect
queryischosenbytheselectionagent.
Fig. 7presentsacomparativeanalysisofsystemcorrectnessacrossmultipledatabases. Thex-axis
lists various databases or categories such as California Schools, Formula 1, and Superhero, while
the y-axis represents the percentage performance. Two key metrics are visualized: the first is the
percentagewherethecorrectanswerexistsamongthecandidates(shownbyonebarpercategory),
andthesecondisthepercentagewherethecorrectanswerischosenbytheselectionsystem(depicted
byasecondbarforeachcategory).
A.7.1 SELECTIONAGENTERRORANALYSIS
Inthissection,weexaminecaseswhereatleastoneofthecandidateSQLqueriesgeneratedbythe
threegeneratorsmatchedthegroundtruthanswer,buttheselectionagentassignedthehighestscore
toanother,incorrectcandidate. Wecategorizedtheseerrorsintofourgroups: (1)Vaguequestions,
(2) Wrong picking, (3) Data Integrity Error, and (4) Incorrect gold query. Fig. 8 illustrates the
distributionofeachcategoryamongthesamplequeries. Inthefollowingsections,wewilldiscuss
eachofthesecategoriesinmoredetail.
Figure 8: Error analysis on the cases where selection agent failed to pick the correct SQL query
whichwasamongthecandidates.
18

## Page 19

PublishedasaconferencepaperatICLR2025
WrongPickingErrors: Thelargestportionoferrorsoccurswhenthecandidatewiththehighest
scorefromtheselectionagentismissingarequiredcolumn,table,orSQLclause. Inouranalysis,
wecouldnotidentifyaspecifictypesofpatternsinthemodel’smistakesasthesemistakesincludes
differenttypesoftheerrorsalmostforeachinstance. Fig. 9providesanexamplewheretheselected
SQL query incorrectly uses * to return all columns, instead of just returning the id as specified in
thegroundtruthanswer.
Question: List all patients who were followed up at the outpatient clinic
who underwent a laboratory test in October 1991 and had a total blood
bilirubin level within the normal range.
Evidence: followed up at the outpatient clinic refers to Admission = '-';
laboratory test in April 1981 refers to Date like '1991-10%'; blood bilirubin
level within the normal range refers to T-BIL < 2.0;
Gold SQL: SELECT DISTINCT T1.ID FROM Patient AS T1 INNER JOIN Laboratory
AS T2 ON T1.ID = T2.ID WHERE T1.Admission = '-' AND T2.`T-BIL` < 2.0 AND
T2.Date LIKE '1991-10-%'
Picked SQL: SELECT DISTINCT T1.* FROM Patient AS T1 INNER JOIN
Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Admission = '-' AND T2.`T-BIL` <
2.0 AND T2.Date LIKE '1991-10%'
Figure9: AnexampleofselectionagentpreferredSQLquerywhichisincorrect.
WrongGoldenQueryError: Thesecondlargestportionoferrorsoccurswhenthegroundtruth
SQLqueryisincorrect,andoneofthecandidatequeriesgeneratedbyourmodelreplicatesthesame
mistake. However,theselectionagentultimatelypicksanothercandidatethatcorrectlyanswersthe
question. Fig. 10 provides an example of such a case, where the ground truth query includes an
extramolecule IDcolumnintheSELECTclause,whichwasnotspecifiedinthequestion.
Question: What are the labels for TR000, TR001 and TR002?
Evidence: TR000, TR001 and TR002 are molecule id; label = '+' mean
molecules are carcinogenic; label = '-' means molecules are non-
carcinogenic
Gold SQL: SELECT molecule_id, T.label FROM molecule AS T WHERE
T.molecule_id IN ('TR000', 'TR001', 'TR002')
Picked SQL: SELECT label FROM molecule WHERE molecule_id IN ('TR000',
'TR001', 'TR002')
Figure10: AnexampleofanerrorcasewheretheselectionagentpickedacorrectSQLqueryand
thegoldquerywaswrong.
VagueQuestion: Anothersignificantportionoferrorsoccurswhenthequestiondoesnotspecify
whichcolumntoreturnoruseforfiltering, andmultiplecolumnscouldsatisfythequery. Inthese
cases,althoughoneofthecandidateswasthecorrectSQLquery,theselectionmodelfavoredanother
responsethatcouldalsobeconsideredcorrect. Fig. 11illustratessuchacasewhere”Fresno”could
refertoeitheracityoracounty,butthequestiondoesn’tspecifywhichonetoreturn. Theselection
modelchosethequerythatused”city”anddidnotselectthecandidatethatused”county.
Question: How many schools in Fresno (directly funded) have number of
test takers not more than 250?
Evidence:
Gold SQL: SELECT COUNT(T1.CDSCode) FROM frpm AS T1 INNER JOIN
satscores AS T2 ON T1.CDSCode = T2.cds WHERE T1.`Charter Funding Type` =
'Directly funded' AND T1.`County Name` = 'Fresno' AND T2.NumTstTakr <=
250
Picked SQL: SELECT COUNT(T1.CDSCode) FROM schools AS T1 INNER JOIN
satscores AS T2 ON T1.CDSCode = T2.cds WHERE T1.City = 'Fresno' AND
T1.FundingType = 'Directly funded' AND T2.NumTstTakr <= 250
Figure11: Anexampleofanerrorcasewheretheselectionmodelpickedaquerywhichcouldbe
consideredascorrectasthequestionisvague.
DataIntegrityError: Finally,thesmallestcategoryoferrorsinvolvescaseswheretwoormore
columnsaresupposedtohaveconsistentvalues, butoneormorecolumnscontainmissingvalues.
19

## Page 20

PublishedasaconferencepaperatICLR2025
For example, Fig. 12 shows a case where the ”School” and ”School Name” columns were both
expectedtocontainthenamesofschools,butoneofthecolumnshasmissingvalues.
Question: List the names of schools with more than 30 difference in
enrollements between K-12 and ages 5-17? Please also give the full street
adress of the schools
Evidence: Diffrence in enrollement = `Enrollment (K-12)` - `Enrollment (Ages
5-17)`
Gold SQL: SELECT T1.School, T1.Street FROM schools AS T1 INNER JOIN frpm
AS T2 ON T1.CDSCode = T2.CDSCode WHERE T2.`Enrollment (K-12)` -
T2.`Enrollment (Ages 5-17)` > 30
Picked SQL: SELECT T2.`School Name`, T1.Street FROM schools AS T1 INNER
JOIN frpm AS T2 ON T1.CDSCode = T2.CDSCode WHERE T2.`Enrollment (K-
12)` - T2.`Enrollment (Ages 5-17)` > 30
Figure 12: An example of an error case where the selection agent picked a correct candidate but
becauseofthedatainconsistencytheexecutionaccuracywaszeroforthiscandidate.
A.7.2 ERRORANALYSES
We present the manual error analysis we conducted on one-third of the cases where none of the
generated candidate queries were correct. We categorized these errors into five main types: (1)
Schemalinkingerrors,(2)Incorrectlogic,(3)SQLfunctionerrors,(4)JOINissues,and(5)Ignoring
evidence. Fig. 13illustratesthedistributionoftheseerrorcategories. Asshown,themostcommon
errorsoccurwhennoneofthecandidatequeriescorrectlyutilizedthecolumnsortablesrequiredto
answerthequestion. Inthefollowingsection,wedescribethespecifictypesoferrorsthatfallunder
eachcategory.
Figure 13: Error analysis on the cases where all candidate generators failed to produce a single
correctanswer.
Schema Linking Errors: The schema linking errors category includes cases where none of the
generatedcandidateSQLqueriescorrectlyusethecolumnsrequiredtoanswerthequestion. These
errorsoftenoccurindatabaseswherecolumnnamesareambiguousorconfusingforthemodel.Fig.
14providesanexamplewheretheLLMfailedtocorrectlycalculatetheaveragetoreturnthecorrect
columnthatwasexpected.
WrongLogicError: Thiscategory,whichrepresentsthesecondlargestportionoferrors,includes
caseswherethelogicofthegeneratedcandidatequeriesisincorrect. Theseerrorsinvolvemissing
elementssuchastheDISTINCTkeyword,NOTNULLconditions,missingcolumnsintheSELECT
clause,orincorrectormissingconditionsintheWHEREorHAVINGclauses.Anexampleisshown
inFig. 15,providesanexamplewheretheLLMfailedtocorrectlycalculatetheaveragetotalprice
duetoincorrectlogiccomputingtheaveragetotalprice.
20

## Page 21

PublishedasaconferencepaperatICLR2025
Question: Who are the top 5 players who perform better in crossing actions?
Indicate their player id.
Evidence: perform better in crossing actions refers to MAX(crossing)
Gold SQL: SELECT id FROM Player_Attributes ORDER BY crossing DESC LIMIT 5
Random Candidate SQL: SELECT player_api_id FROM Player_Attributes ORDER
BY `crossing` DESC LIMIT 5
Figure14: Anexampleofschemalinkingerrorcategory.
Question: What is the average total price of the transactions taken place in
gas stations in the Czech Republic?
Evidence: Gas station in the Czech Republic implies that Country = 'CZE'
Gold SQL: SELECT AVG(T1.Price) FROM transactions_1k AS T1 INNER JOIN
gasstations AS T2 ON T1.GasStationID = T2.GasStationID WHERE T2.Country
= 'CZE'
Random Candidate SQL: SELECT AVG(T1.Amount * T1.Price) FROM
transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.GasStationID =
T2.GasStationID WHERE T2.Country = 'CZE'
Figure15: Anexampleofwronglogicerrorcategory.
SQL Functions Error: This category, the third-largest source of errors, includes queries where
theerrorresultsfromtheincorrectuseof, orfailuretoinclude, SQLfunctionssuchasCOUNT(),
CAST(), AVG(), ROUND(), and others. Fig. 16 illustrates a case where none of the candidate
queriesusedtheROUND()functionasrequiredbythequestion.
Question: How much of the hydrogen in molecule TR206 is accounted for?
Please provide your answer as a percentage with four decimal places.
Evidence: hydrogen refers to element = 'h'; TR206 is the molecule id;
percentage = DIVIDE(SUM(element = 'h'), COUNT(atom_id)) as percent
where molecule_id = 'TR206'
Gold SQL: SELECT ROUND(CAST(COUNT(CASE WHEN T.element = 'h' THEN
T.atom_id ELSE NULL END) AS REAL) * 100 / COUNT(T.atom_id),4) FROM atom
AS T WHERE T.molecule_id = 'TR206'
Random Candidate SQL: SELECT CAST(SUM(CASE WHEN T1.element = 'h'
THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.atom_id) FROM atom AS T1
WHERE T1.molecule_id = 'TR206'
Figure16: AnexampleofwrongusageofSQLfunctionserrorcategory.
JoinsError: Thiscategoryrepresentsasmallerportionoftheerrorcases,wherethesourceofthe
errorismissingoneormoretablesintheJOINclausesofthepredictedSQLqueries.
IgnoringEvidenceError: Thiscategoryrepresentsthesmallestportionoferrorcases,wherethe
correctcolumnortableisexplicitlymentionedintheprovidedevidence,buttheLLMdisregardsit
andusesitsownselectioninstead.
A.8 DIVIDEANDCONQUERPROMPT
Inthissection,weprovideanexampleofadivide-and-conquerpromptusedinoneofthefew-shot
in-contextlearningdemonstrationstoillustratethedecompositionandaggregationsteps.
21

## Page 22

PublishedasaconferencepaperatICLR2025
DatabaseInfo
{DATABASE SCHEMA}
**************************
Question
Question: What is the gender of the youngest client who opened account in the lowest average
salarybranch?
Hint: GiventhatLaterbirthdatereferstoyoungerage;A11referstoaveragesalary
**************************
**1. DivideandConquer:**
* **Main Question:** What is the gender of the youngest client who opened account in
thelowestaveragesalarybranch?
***Analysis:**Questionaskingabout‘gender‘,anditappearsintable‘client‘. Wewillusethis
astheoutputcolumn,selectingitfromtheyoungestclientinthelowestaveragesalarybranch.
***PseudoSQL:**SELECT‘T1‘.‘gender‘FROM‘client‘AS‘T1‘WHEREyoungestclientin
thelowestaveragesalarybranch
***Sub-question1:**youngestclientinthelowestaveragesalarybranch
***Analysis:**Accordingtothehint,weneedtousethe‘A11‘from‘district‘togetthesalary
info,andtheyoungestclientcanbeobtainedfromusingthe‘birth date‘columnoftable‘client‘.
TheitemsbetweenthesetwotablescanbeINNERJOINusingdistrict id.
* **Pseudo SQL:** SELECT ‘T1‘.‘client id‘ FROM ‘client‘ AS ‘T1‘ INNER JOIN ‘district‘
AS‘T2‘ON‘T1‘.‘district id‘=‘T2‘.‘district id‘WHERElowestaveragesalarybranchORDER
BY‘T1‘.‘birth date‘DESCNULLSLASTLIMIT1
***Sub-question1.1:**lowestaveragesalarybranch
***Analysis:**Wecangetthelowestaveragesalarybranchusingorderby‘A11‘ASCandpick
top1. Thecolumn‘A11‘isnotNULLABLE,sowedonotneedtoadd”ISNOTNULL”filter*
**PseudoSQL:**SELECT‘district id‘FROM‘district‘ORDERBY‘A11‘ASCLIMIT1
**2. AssemblingSQL:**
* **Sub-question 1.1 (lowest average salary branch):** * **SQL:** SELECT ‘district id‘
FROM‘district‘ORDERBY‘A11‘ASCLIMIT1
***Sub-question1(youngestclientinthelowestaveragesalarybranch):**
* **SQL:** SELECT ‘T1‘.‘client id‘ FROM ‘client‘ AS ‘T1‘ INNER JOIN ‘district‘ AS ‘T2‘
ON ‘T1‘.‘district id‘ = ‘T2‘.‘district id‘ WHERE ‘T2‘.‘district id‘ IN (SELECT ‘district id‘
FROM‘district‘ORDERBY‘A11‘ASCLIMIT1)ORDERBY‘T1‘.‘birth date‘DESCNULLS
LASTLIMIT1
***MainQuestion(genderoftheclient):**
* **SQL:** SELECT ‘T1‘.‘gender‘ FROM ‘client‘ AS ‘T1‘ WHERE ‘T1‘.‘client id‘ =
(SELECT ‘T1‘.‘client id‘ FROM ‘client‘ AS ‘T1‘ INNER JOIN ‘district‘ AS ‘T2‘ ON
‘T1‘.‘district id‘=‘T2‘.‘district id‘WHERE‘T2‘.‘district id‘IN(SELECT‘district id‘FROM
‘district‘ORDERBY‘A11‘ASCLIMIT1)ORDERBY‘T1‘.‘birth date‘DESCNULLSLAST
LIMIT1)
**3. SimplificationandOptimization:**
* The nested queries can be combined using a single ‘INNER JOIN‘ and the filtering can be
donewithinasingle‘ORDERBY‘clause.
**FinalOptimizedSQLQuery:**
SELECT ‘T1‘.‘gender‘ FROM ‘client‘ AS ‘T1‘ INNER JOIN ‘district‘ AS ‘T2‘ ON
‘T1‘.‘district id‘ = ‘T2‘.‘district id‘ ORDER BY ‘T2‘.‘A11‘ ASC, ‘T1‘.‘birth date‘ DESC
NULLSLASTLIMIT1
Figure17: AnexampleofthedivideandconquerCoTmethod
22

## Page 23

PublishedasaconferencepaperatICLR2025
Anexampleofquestion/SQLpairwherethedivide-and-conquerCoTapproachwastheonlygener-
atorthatsolvedtheproblem.
Question: How much faster in percentage is the champion than the driver
who finished the race last in the 2008 Australian Grand Prix?
Query:
WITH time_in_seconds AS (
SELECT
T1.positionOrder,
CASE
WHEN T1.positionOrder = 1 THEN
(CAST(SUBSTR(T1.time, 1, 1) AS REAL) * 3600) +
(CAST(SUBSTR(T1.time, 3, 2) AS REAL) * 60) +
CAST(SUBSTR(T1.time, 6) AS REAL)
ELSE
CAST(SUBSTR(T1.time, 2) AS REAL)
END AS time_seconds
FROM
results AS T1
INNER JOIN
races AS T2
ON T1.raceId = T2.raceId
WHERE
T2.name = 'Australian Grand Prix'
AND T1.time IS NOT NULL
AND T2.year = 2008
),
champion_time AS (
SELECT time_seconds
FROM time_in_seconds
WHERE positionOrder = 1
),
last_driver_incremental AS (
SELECT time_seconds
FROM time_in_seconds
WHERE positionOrder = (
SELECT MAX(positionOrder)
FROM time_in_seconds
)
)
SELECT
(CAST((SELECT time_seconds FROM last_driver_incremental) AS REAL) *
100) /
(SELECT time_seconds +
(SELECT time_seconds FROM last_driver_incremental)
FROM champion_time);
Figure18: AnexampleofquerythathasbeensolvedonlywiththedivideandconquerCoTmethod.
23

## Page 24

PublishedasaconferencepaperatICLR2025
A.9 QUERYPLANPROMPT
Inthissection,weprovideanexampleofaquery(execution)planpromptusedinoneofthefew-shot
in-contextlearningdemonstrationstoillustratethesteps.
DatabaseInfo
{DATABASE SCHEMA}
**************************
AnswerRepeatingthequestionandevidence,andgeneratingtheSQLwithaqueryplan.
**Question**: HowmanyThairestaurantscanbefoundinSanPabloAve,Albany?
**Evidence**: Thai restaurant refers to food type = ’thai’; San Pablo Ave Albany refers to
street name=’sanpabloave’ANDT1.city=’albany’
**QueryPlan**:
**PreparationSteps:**
1. Initializetheprocess: Startpreparingtoexecutethequery.
2. Preparestorage: Setupstoragespace(registers)toholdtemporaryresults,initializingthemto
NULL.
3. Openthelocationtable: Openthelocationtablesowecanreadfromit.
4. Openthegeneralinfotable: Openthegeneralinfotablesowecanreadfromit.
**MatchingRestaurants:**
1. Startreadingthelocationtable: Movetothefirstrowinthelocationtable.
2. Checkifthestreetmatches: Lookatthestreet namecolumnofthecurrentrowinlocation. If
it’snot”sanpabloave,”skipthisrow.
3. Identifythematchingrow: Storetheidentifier(rowID)ofthislocationentry.
4. Findthecorrespondingrowingeneralinfo: UsetherowIDfromlocationtodirectlyfindthe
matchingrowingeneralinfo.
5. Checkifthefoodtypematches:Lookatthefood typecolumningeneralinfo. Ifit’snot”thai,”
skipthisrow.
6. Check if the city matches: Look at the city column in generalinfo. If it’s not ”albany,” skip
thisrow.
**CountingRestaurants:**
1. Preparetocountthismatch: Ifallcheckspass,preparetoincludethisrowinthefinalcount.
2. Countthismatch: Incrementthecountforeachrowthatmeetsallthecriteria.
3. Move to the next row in location: Go back to the location table and move to the next row,
repeatingtheprocessuntilallrowsarechecked.
4. Finalizethecount: Onceallrowshavebeenchecked,finalizethecountofmatchingrows.
5. Preparetheresult: Copythefinalcounttoprepareitforoutput.
**DeliveringtheResult:**
1. Outputtheresult: Outputthefinalcount,whichisthenumberofrestaurantsthatmatchallthe
specifiedcriteria.
2. Endtheprocess: Stopthequeryexecutionprocess.
3. Setup phase: Before starting the actual query execution, the system prepares the specific
valuesitwillbelookingfor,like”sanpabloave,””thai,”and”albany.”
**FinalOptimizedSQLQuery:**
SELECT COUNT(T1.id restaurant) FROM generalinfo AS T1 INNER JOIN location AS
T2 ON T1.id restaurant = T2.id restaurant WHERE T1.food type = ’thai’ AND T1.city =
’albany’ANDT2.street name=’sanpabloave’
Figure19: AnexampleofthequeryplanCoTmethod
24

## Page 25

PublishedasaconferencepaperatICLR2025
Fig. 20providesanexampleofaqueryplangeneratedbyusingtheEXPLAINcommand.
Figure20: AnexampleofSQLitequeryplangeneratedbyusingtheEXPLAINcommand.
AdditionallyFig. 21providesanexamplequestionthatwassolvedbyusingthequeryplan-based
CoTstrategy.
Question: State the names and full communication address of high schools
in Monterey which has more than 800 free or reduced price meals for ages
15-17?
Query Plan CoT SQL:
SELECT T1.`School Name`, T2.Street, T2.City, T2.State, T2.Zip
FROM frpm AS T1
INNER JOIN schools AS T2 ON T1.CDSCode = T2.CDSCode
WHERE T1.`County Name` = 'Monterey' AND T1.`Free Meal Count (Ages 5-17)`
> 800 AND T1.`School Type` = 'High Schools (Public)';
Divide and Conquer CoT SQL:
SELECT `T1`.`School Name`, `T2`.`Street`, `T2`.`City`, `T2`.`State`, `T2`.`Zip`
FROM `frpm` AS `T1`
INNER JOIN `schools` AS `T2` ON `T1`.`CDSCode` = `T2`.`CDSCode`
WHERE `T2`.`SOCType` = 'High Schools (Public)' AND `T2`.`County` =
'Monterey' AND `T1`.`FRPM Count (Ages 5-17)` > 800
Figure21: AnexampleofquerythathasbeensolvedonlywiththequeryplanCoTmethod.
25

## Page 26

PublishedasaconferencepaperatICLR2025
A.10 QUERYFIXINGPROMPT
Inthissection,weprovidetheprompttemplatefortheSQLqueryfixingstep.
**TaskDescription:**
You are an SQL database expert tasked with correcting a SQL query. A previous attempt to
run a query did not yield the correct results, either due to errors in execution or because the
resultreturnedwasemptyorunexpected. Yourroleistoanalyzetheerrorbasedontheprovided
databaseschemaandthedetailsofthefailedexecution,andthenprovideacorrectedversionof
theSQLquery.
**Procedure:**
1. ReviewDatabaseSchema:
-Examinethetablecreationstatementstounderstandthedatabasestructure.
2. AnalyzeQueryRequirements:
-OriginalQuestion: Considerwhatinformationthequeryissupposedtoretrieve.
- Hint: Use the provided hints to understand the relationships and conditions relevant to the
query.
-ExecutedSQLQuery: ReviewtheSQLquerythatwaspreviouslyexecutedandledtoanerror
orincorrectresult.
- Execution Result: Analyze the outcome of the executed query to identify why it failed (e.g.,
syntaxerrors,incorrectcolumnreferences,logicalmistakes).
3. CorrecttheQuery:
- Modify the SQL query to address the identified issues, ensuring it correctly fetches the
requesteddataaccordingtothedatabaseschemaandqueryrequirements.
**OutputFormat:**
Present your corrected query as a single line of SQL code, after Final Answer. Ensure
therearenolinebreakswithinthequery.
Herearesomeexamples:
{EXAMPLES}
=======Yourtask=======
**************************
Tablecreationstatements
{DATABASE SCHEMA}
**************************
Theoriginalquestionis:
Question:
{QUESTION}
Evidence:
{HINT}
TheSQLqueryexecutedwas:
{QUERY}
Theexecutionresult:
{RESULT}
**************************
Basedonthequestion,tableschemaandthepreviousquery,analyzetheresulttrytofixthequery.
Figure22: Theprompttemplateusedforqueryfixing
26

## Page 27

PublishedasaconferencepaperatICLR2025
A.11 SELECTIONAGENTPROMPT
Inthissection,weprovidetheprompttemplateusedfortrainingandquerypickingattesttimebythe
trainedselectionagent. Notethatthedatabaseschemausedinthisstepistheunionofthecolumns
andtablesbythetwocandidatesinsteadofusingthefull-schemaofalltablesinthedatabase.
Instruction:
Given the DB info and question, there are two candidate queries. There is correct one and
incorrectone, comparethetwocandidateanswers, analyzethedifferencesofthequeryandthe
result. Basedontheoriginalquestionandtheprovideddatabaseinfo,choosethecorrectone.
**************************
DatabaseSchema
{DATABASE SCHEMA}
**************************
Question:
{QUESTION}
Evidence:
{HINT}
**************************
CandidateA
{CANDIDATE A QUERY}
Executionresult
{CANDIDATE A RESULT}
**************************
CandidateB
{CANDIDATE B QUERY}
Executionresult
{CANDIDATE B RESULT}
Justoutputthecorrectanswer”A”or”B”.
Figure23: Theprompttemplateusedforqueryfixing
27

## Page 28

PublishedasaconferencepaperatICLR2025
A.12 GENERATEDSYNTHETICEXAMPLESANALYSIS
Figure24: Syntheticexamplesgeneratedforthe‘california schools‘databasequestionwithdifferentguide-
linesforcommonSQLfeaturesandfilteredcolumns.
Table 8: Ablationstudiesonsyntheticexamplegenerationguidelines, R withcommonSQLfeaturesand
f
R withfilteredschema. ThebaselineistheoriginalBIRDpromptZero-shotCoTwithGemini1.5proonthe
t
BIRDdevset.Totalof75examplesaregeneratedforeachexampleset(R ,R )andforthemixed(R +R )
f t f t
Method ExecutionAccuracy(%) ∆(%)
Baseline(Zero-shot) 57.75 -
OSw/R 65.45 +7.7
f
OSw/R 66.75 +9.0
t
OSw/R +R 67.09 +9.34
f t
Table 8 illustrates the ablation studies done with different guidelines and their generated example
sets. Compared to the baseline (no example), the user question and its associated data schema
targettedsyntheticexamplescanhelp;wetrytopromotethediversityoftheexamplestoavoidover-
fittingtheoutputtocertainpatterns(e.g.,themodelalwayswritesaSQLwithJOINifshownmostly
JOINexamples).
Figure25:Distribution(normalized)ofsyntheticvs.groundtruthexamplesindifferentSQLfeatures/clauses.
All examples are generated using gemini-1.5-pro for the questions and schemas from the BIRD-Bench dev
dataset.
(b)Syntheticexamplesfollowingcross-domaindata
(a) Our synthetic examples with explicit guidelines,
R andR augmentationstrategy(Lietal.,2024b)
f t
Fig. 25ashowstheSQLfeaturedistributionofthegeneratedsyntheticexamplesfortheBIRDdev
dataset, which closely follows the actual SQL features distribution, except CASE statement. We
28

## Page 29

PublishedasaconferencepaperatICLR2025
omit CASE statement examples, since showing examples with CASE statement did not help with
thegeneration,unlesstheground-truthSQLqueryactuallyusedit.
Table9: Examplequalitycomparisonbetweenoursyntheticexamples(OS)andotherexamplesets,prepared
bytwootherapproaches: relevanttrainingexamplesbyquestionsimilarity(σ(train))andadifferentsynthetic
example generation strategy (CodeS). To isolate the impact of example quality, we only generated a single
outputcandidatewithoutanyself-correctionwithvaryingnumbersofexamplesn.
n 5 25 75 125
σ(train) 58.80 58.54 57.69 56.91
CodeS 60.76 60.63 59.97 59.06
OS 62.13 64.02 64.41 63.69
Table9demonstrateshowtheonlinesyntheticexamplegeneration(OS)yieldsmoreusefulexample
setforin-contextlearning,comparedtotwootherapproaches. Trainingdatasetisacommonlyused
source of few-shot examples, where examples are selected by question similarity (σ(train)). Data
augmentationisanothertechniqueusedforcross-domainadaptation,whereeitherextrafine-tuning
data or few-shot examples are synthesized.The proposed technique in (Li et al., 2024b) uses two-
step example generation, where the model is 1) asked to come up with questions to ask given the
schema; 2)askedtofillintheblanksofexampletemplateswiththeschemaelements. Thereisno
specific guidelines to the example and SQl structures for the first step, and the second step uses a
setofuniversalquestion/SQLtemplateswithlimitedcomplexity(e.g.,onlysingletable,non-nested
querieswithupto3columns). TheresultingexampleSQLfeaturedistributionisshowninFig. 25b.
29

## Page 30

PublishedasaconferencepaperatICLR2025
A.13 SYNTHETICEXAMPLEGENERATIONPROMPTS
Inthissectionweprovidedtheprompttemplatefortheonlinesyntheticexamplegenerationstep.
YouareaSQLiteSQLexpert. Yourjobistocreate{k}examples,whereeachexampleconsists
of a question and a SQL query to fetch the data for it. I want each example to look like this,
questioninputandSQLoutputpairs:
```
”input”: ”What’sthedescriptionoftheseriescodeSM.POP.TOTLforAruba?
(Hints: ArubaisthenameofthecountrywhereShortName=’Aruba’)”
”output”: ”SELECT T2.Description FROM Country AS T1 INNER JOIN CountryNotes
AS T2 ON T1.CountryCode = T2.Countrycode WHERE T1.ShortName = ’Aruba’ AND
T2.Seriescode=’SM.POP.TOTL’”
```
You should generate examples that examine and showcase different aspects and relation-
ships of the following table schemas, described in ”Table creation statements”. Understand the
databasetablesandtheirrelationships. Understandthecolumnsandtheirtypesandmeaningsto
constructintrestingexamples.
GenerateamixtureofSQLexamplesthatinclude:
• somesimpleSQLqueryexampleswithoutJOIN
• someSQLqueryexampleswithaggregates,likeCOUNT
• somesimpleSQLqueryexampleswithJOIN
• somecomplexSQLqueryexampleswithnestedJOIN
**************************
###Tablecreationstatements###
{TARGET DATABASE SCHEMA}
**************************
Generate total of {k} examples. Only outputs the examples (question input and SQL output
pairs),andeachexamplecanbeseparatedbyanewline.
Figure26: SyntheticexamplegenerationpromptusedforcommonSQLfeaturesexamplesgenera-
tion. TARGET DATABASE SCHEMAcontainsallthetablesfromthetargetdatabase.
30

## Page 31

PublishedasaconferencepaperatICLR2025
You are a SQLite SQL expert. Your job is to create a set of examples, where each example
consistsofaquestionandaSQLquerytofetchthedataforit.
Youshouldgenerateexamplesthatexamineandshowcasedifferentaspectsandrelationshipsof
thefollowingtableschemas. Understandthedatabasetablesandtheirrelationships. Understand
thecolumnsandtheirtypesandmeaningstoconstructintrestingexamples.
Iwillalsoshowyoumultipleexamplesgeneratedfortheotherdatabaseanditstableschemas,so
youcanseewhatkindofexamplescanbegeneratedforagivendatabase.
**************************
###Examplesfromotherdatabase###Thefollowingisthetableschemasandcolumnexamples
forotherdatabase:
The database ({¨TRAIN DATABASE NAME}¨) structure is defined by the following table
schemas(commentsafter’–’provideadditionalcolumndescriptions).
{TRAIN DATABASE SCHEMA}
————————–
Thefolloiwingaretheexamplesgeneratedfortheabovedatabaseschemas:
Example1)”input”:”AmongthecountriesinthegroupofHeavilyIndebtedPoorCountries,how
manyofthemareunderthelendingcategoryoftheInternationalDevelopmentAssociations?
(Hints: group of Heavily Indebted Poor Countries is OtherGroups = ’HIPC’; International
DevelopmentAssociationsreferstolendingcategory=’IDA’)”
”output”: ”SELECT COUNT(CountryCode) FROM Country WHERE LendingCategory =
’IDA’ANDOtherGroups=’HIPC’”
...
Example 10) ”input”: ”What is the description of the footnote on the series code
AG.LND.FRST.K2in1990forAruba?
(Hints: Year=1990;ArubaisthenameofcountrywhereShortName=’Aruba’)”
”output”: ”SELECTT2.DescriptionFROMCountryAST1INNERJOINFootNotesAST2ON
T1.CountryCode = T2.Countrycode WHERE T1.ShortName = ’Aruba’ AND T2.Seriescode =
’AG.LND.FRST.K2’ANDT2.Year=’YR1990’”
**************************
Now similarly, generate examples (question input and SQL output pairs) for the table schemas
definedbelow,in”Tablecreationstatements”.
**************************
###Tablecreationstatements###
TARGET DATABASE SCHEMA
**************************
Only outputs the examples (question input and SQL output pairs), and each example can be
separatedbyanewline.
Figure 27: Synthetic example generation prompt. This is use TARGET DATABASE SCHEMA
filteredwithcolumnselectionresult,andthemodelisaskedtogeneratesimpleexamplessimilarto
theonestakenfromthetrainingdataset(separatefromthetestordevdataset).
31