# Top-K Representative Search for Comparative Tree Summarization

## Page 1

IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING, VOL. 37, NO. 8, AUGUST 2025
4873
Top-K Representative Search for Comparative
Tree Summarization
Yuqi Chen
, Xin Huang
, and Bilian Chen
Abstract—Data summarization aims at utilizing a small-scale
summary to represent massive datasets as a whole, which is useful
for visualization and information sipped generation. However, most
existing studies of hierarchical summarization only work on one
single tree by selecting k representative nodes, which neglects an
important problem of comparative summarization on two trees. In
this paper, given two trees with the same topology structure and
different node weights, we aim at ﬁnding k representative nodes,
where k1 nodes summarize the common relationship between them
and k2 nodes highlight signiﬁcantly different subtrees meanwhile
satisfying k1 + k2 = k. To optimize summarization results, we
introduce a scaling coefﬁcient for balancing the summary view
between two subtrees in terms of similarity and difference. Ad-
ditionally, we propose a novel deﬁnition based on the Hellinger
distance to quantify the node distribution difference between two
subtrees. We present a greedy algorithm SVDT to ﬁnd high-quality
results with approximation guaranteed in an efﬁcient way. Further-
more, we explore an extension of our comparative summarization
to handle two trees with different structures. Extensive experiments
demonstratetheeffectivenessandefﬁciencyofourSVDTalgorithm
against existing summarization competitors.
Index
Terms—Tree
summarization,
top-k
diversiﬁcation,
hellinger distance.
I. INTRODUCTION
G
RAPHS composed of nodes and edges are often used to
depict complex datasets [2], [3]. Graph visualization gives
a simpliﬁed presentation with an intuitive overview for users.
However, graphs can only enhance understanding if the size of
summary answers is small enough in a manageable scale for
human comprehension [1].
In this paper, we study a novel problem of differential tree
summarization to depict the similarities and differences between
two trees, which aims to show two trees’ homogeneity and
heterogeneity using a small summary answer. Let us consider a
real example of an academic conference SIGMOD with several
research sessions and papers. Fig. 1(a) shows two instance trees
T1 and T2 representing the SIGMOD’19 conference, where the
node weight represents the number of downloads of a research
Received 28 June 2024; revised 25 February 2025; accepted 16 April 2025.
Date of publication 9 May 2025; date of current version 7 July 2025. This work
was supported by the Hong Kong RGC Projects under Grant 12200021 and
Grant C2003-23Y and in part by the National Natural Science Foundation of
China under Grant 12371515. Recommended for acceptance by S. Salihoglu.
(Corresponding authors: Xin Huang; Bilian Chen.)
Yuqi Chen and Xin Huang are with the Hong Kong Baptist University,
Hong Kong, China (e-mail: csyqchen@comp.hkbu.edu.hk; xinhuang@comp.
hkbu.edu.hk).
Bilian Chen is with the Department of Automation, Xiamen University, Fujian
361005, China (e-mail: blchen@xmu.edu.cn).
Digital Object Identiﬁer 10.1109/TKDE.2025.3565845
Fig. 1.
A running example of comparative tree summarization.
paper at different periods of 2019-2020 and 2019-2024, respec-
tively.T1 andT2 havethesamestructure,whichhasfourresearch
sessions of MH, IE, DI, ML, and 12 research papers (p1, p2 . . .,
p12), but having different node weights. Speciﬁcally, p1[a], p2[b],
p3[c] are three research papers belonging to the research session
of MH (modern hardware). Note that the weights of four research
session nodes are the average download of this session’s papers,
to fairly represent the hotness of each research session.
The objective of our differential summarization is to select
the most k attractive or unpopular research topics and papers
to distinguish the conference SIGMOD’19 in the recent four
years from 2020 to 2024. We set a small number k = 5. The
existing three different methods of FEQ [1], CAGG [1], and
GVDO
[5] ﬁnd the answers of ﬁve most attractive papers,
as shown in Figs. 1(b), 1(c), 1(d), respectively. It lacks of
identifying research sessions or speciﬁc papers that have gone
from niche to popular, which fails to capture the changes in a
summarized way. In contrast, our method can capture distinctive
features between two trees with the same structure, as shown in
Fig. 1(e). The answer includes r, DI, ML, p7 and p11. The nodes
contributing to homogeneous summarization are in red, while
nodes contributing to differential summarization are in blue. The
darker the node color, the more the node’s contribution to the
attribute it represents.
r Homogeneous summarization: This involves two nodes r,
p11[d]. Node p11 is labeled in light red, indicating that
[a]Prasaad et al. Concurrent preﬁx recovery..., In SIGMOD, 2019.
[b]Zhang et al. Briskstream: Scaling data stream..., In SIGMOD, 2019.
[c]Kim et al. Border-collie: a wait-free..., In SIGMOD, 2019.
[d]Shang et al. Democratizing data science..., In SIGMOD, 2019.
© 2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see
https://creativecommons.org/licenses/by/4.0/



## Page 2

4874
IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING, VOL. 37, NO. 8, AUGUST 2025
this machine learning-related paper has been consistently
popular from 2020 to 2024.
r Differential summarization: This involves three nodes DI,
ML, p7[e]. Both of the nodes DI and ML in dark blue with
their direct ancestor node r in dark red represent signif-
icant changes in data integration and machine learning,
representing that these two sessions become increasingly
popular from 2020 to 2024. The node p7 is marked in light
blue, meaning that from low at the beginning to very high
later on, we ﬁnd it is the best paper of SIGMOD’19.
Beside the application of differential summarization on SIG-
MOD research topic, we illustrate two more typical applications
as follows. First, consider a disease ontology [5], the hierarchical
tree consists of disease categories (e.g. cancer, mental health
disease, syndrome disease, cellular proliferation disease). In
turn, the category of ‘cancer’ may have speciﬁc instances of
‘lung cancer’ and ‘leukemia’. Given one hospital with different
disease distributions on this disease ontology over a few years,
the differential summarization reveals the common disease pat-
terns and the change trends of disease occurrence. Similarly, one
more application is summarizing university admission statis-
tics. A university hierarchy comprises several faculties (e.g.
science, medicine, law). In turn, the faculty of science may
have sub-institutional departments (e.g. mathematics, physics,
chemistry). Summarizing two university hierarchies with dif-
ferent admission numbers over years helps identify stable major
disciplines and emerging popular subjects, e.g., data science and
AI.
In light of the above, the differential summary in Fig. 1(e)
is a concise answer to well preserve the homogeneity and
difference in T1 and T2. However, the problem of differential
summarization has two challenges. First, it is hard to determine
the number of homogeneous and differential nodes although the
total number k is given. Second, it is not easy to design a uniﬁed
summary score function to similarity and difference simulta-
neously by incorporating the weight distributions in subtrees.
To tackle them, we propose a fast algorithm for differential
summarization based on a new concept of distribution score
Distri(·) using Hellinger distance [12], which uses a scaling
coefﬁcient to balance. To summarize, this paper makes the
following contributions:
r The problem we study is to choose a small set of elements
to summarize two large-scale and hierarchically structured
trees. We deﬁne the kVDT problem for ﬁnding represen-
tative nodes for similarity and difference summarization
by considering the diverse representation across subtrees’
weight distribution (Section III).
r We propose an efﬁcient Hellinger distance-based distribu-
tion calculation to quantify the node distribution distance
between two subtrees. Furthermore, we introduce a sum-
mary visualization technique that converts the output of
our method into a concise and visually comprehensible
tree summary (Section IV).
r We conduct extensive experiments on real-world datasets,
including a case study and a usability study, to validate
[e]Salimi et al. Interventional fairness: Causal..., In SIGMOD, 2019.
the feasibility and effectiveness of our algorithm against
competitors (Section V).
II. RELATED WORK
Graph summarization has been studied widely in the liter-
ature [4], [6], [8], [10], [11]. Navlakha et al. [8] proposed a
graph compression method to generate graph summary with
edge corrections. To enhance efﬁciency, Chu et al. [6] improved
Navlakha’s approach by identifying and merging pairs with
high saving values. Wu et al. [10] considered topology and
feature similarity for summarizing attributed graphs, but led to
a graph recovery error rate. Kumar et al. [11] and Lee et al. [9]
addressed this problem from different perspectives, the former
focused on utility-driven to ensure the graph summary meet a
user-speciﬁed utility threshold, while the latter achieved lossless
summarization by representing unweighted graphs using posi-
tive and negative edges between hierarchical supernodes. Huang
et al. [4] proposed GVDO algorithm to visualize a summary
graph in the ontology structure. TS algorithm [7] was introduced
for efﬁciently summarizing hierarchical multidimensional data.
Different from most existing studies above that focus on a single
graph, our study aims at differential summarization by ﬁnding
k similar and different representatives on two trees.
III. PROBLEM STATEMENT
In this section, we present our problem and notions.
Preliminaries: Given a tree T = (V, E, freq), which con-
tains V nodes and E edges, and freq is a non-negative integer
function of the node weight. We introduce the node set S1 ⊆V
representing similarity, and the node set S2 ⊆V representing
difference. S1 ∩S2 = ∅, and their union S = S1 ∪S2 serves as
the set of selected nodes for summarization. We consider two
instances of trees T1 and T2 with different weights. Note that, in
this paper, anc(x) represents the ancestors of x which include
x itself, while des(x) represents x itself with the descendants of
x.
To capture the representative effect of nodes and their de-
scendants at different levels, we consider the distance denoted
as disx(y) between them. disx(y) only exists when y ∈des(x).
Otherwise, it is set to 0. The distance disx(y) can be calculated
using the following formula.
disx(y) =

1
level(y)−level(x)+1, if y ∈des(x)
0, otherwise
Example 1:
Consider the tree T(V, E) in Fig. 1(a). For
nodes p1 and r, the function level(·) is deﬁned as level(x) =
distT (x, r0), representing the level distance from the root r0 to
the node x in tree T. Thus, level(p1) = 2 and level(r) = 0, and
the distance disr(p1) = 1/3.
To balance the similarity and difference in summary views,
we introduce the scaling coefﬁcient γ.
Deﬁnition 1 (Scaling Coefﬁcient): Given two weighted trees
T1, T2, the scaling coefﬁcient represented by γ is obtained by
calculating the average ratio of similarity and difference of all



## Page 3

CHEN et al.: TOP-K REPRESENTATIVE SEARCH FOR COMPARATIVE TREE SUMMARIZATION
4875
TABLE I
FREQUENTLY USED NOTATIONS IN THIS PAPER
nodes satisfying x ∈V.
γ = 1
|V|

x∈V
min(freqT1(x), freqT2(x))
|freqT1(x) −freqT2(x)|
(1)
Note that Eq. (1) ignores the case of node x with freqT1(x) =
freqT2(x). Similar computations are also applied to other met-
rics throughout this paper. In practical applications, there are
signiﬁcant differences in homogeneous and heterogeneous sum-
marizationduetovaryingfrequenciesandhierarchicalstructures
of datasets.
Representative score: For two nodes x, y satisfying y ∈
des(x), we deﬁne simRepx(y) and difRepx(y) to measure
representative similarity and difference score of x on y in T1
and T2, respectively. Note that scaling coefﬁcient γ is only used
in the difference measure formula to adjust the imbalance of the
similarity and difference between nodes.
simRepx(y) = min (freqT1(y), freqT2(y)) · disx(y)
(2)
difRepx(y) = |freqT1(y) −freqT2(y)| · γ · disx(y)
(3)
This paper addresses the kVDT problem, which selects k
representative nodes for Visualizing similarity and Difference
on hierarchical Tree structure as follows.
The kVDT-problem statement: Given two trees T1, T2 with
different weights and a positive integer k, the problem is to ﬁnd
a k-sized representative set S ⊆V such that S = S1 ∪S2, where
S1 consists of k1 similarity representatives and S2 consists of k2
difference representatives, ensuring that S reaches the maximum
summary score with |S| = k. Table I lists the notations usually
used in this paper.
IV. SVDT ALGORITHM
In this section, we ﬁrst introduce a novel concept of nor-
malized distribution score comparing similarity and difference.
Based on it, we deﬁne our summary score function and prove its
submodularity. Leveraging the submodular property, we develop
a greedy algorithm SVDT and introduce the summary visual
representation based on SVDT results. Finally, we discuss an
extension of our techniques to handle differential summarization
on two trees with different structures.
A. Distribution Normalization of Non-Leaf Nodes
In our problem formulation, we consider the distribution of
nodes with their descendants. The key of comparing a represen-
tative node x in two trees T1, T2 is to measure the similarity
and difference of their representative normalized distribution
in x’s subtree. Here, we use a parameter β ∈Z+ to be the
number of representative similar and different weights, i.e.,
SimD(x) = [SimT1
1 (x), SimT2
1 (x), . . . , SimT2
β (x)], DifD(x)
= [Dif T1
1 (x), Dif T1
1 (x), . . . , Dif T2
β (x)], respectively. These
two distributions can be efﬁciently computed from the non-leaf
nodes at the bottom level, i.e., progressively passing up top-β
similar and differential distributions from the bottom upwards
until reaching the root.
Example 2: Fig. 2 illustrates the distribution normalization
of non-leaf nodes in detail. T1 and T2 share the same hierarchical
structure but differ in weight values in Fig. 2(a). We consider
common node weights as similarity values by Eq. (2) and
weight differences as difference values by Eq. (3). For passing
upward, we select top-1 node each from similarity and difference
distributions in Fig. 2(b). Speciﬁcally, starting from the lowest
non-leaf nodes, that is, node A, with its direct descendants
{A, a1, a2, a3}, we select the node a2 that best represents sim-
ilarity and a3 that best represents difference. Their frequencies
in T1 and T2 form distributions for the node A. Accordingly, the
distribution for the non-leaf node B is represented by the fre-
quenciesofthemostsimilarnodeb2 andthemostdissimilarnode
b3 in T1 and T2. Therefore, we obtain SimD(A), DifD(A),
SimD(B), DifD(B). Then, we proceed to pass upwards. For
the root node r, with the nodes A and B as its direct descendants,
we search for the distribution that best represents homogeneity
and difference within {r, A, B}, which are obviously SimD(B)
and DifD(A). Therefore, the distribution representing node r
is SimD(r)=[50, 45], DifD(r)=[100, 0].
Computing distribution score Distri(·): After obtaining
SimD(·) and DifD(·) for all non-leaf nodes in Fig. 2(b), we
proceed with the normalization to obtain SimD(·) and DifD(·)
for all non-leaf nodes in Fig. 2(c). After converting them to
probability distributions, we apply the Hellinger distance [12]
to calculate the distance between similarity distribution and
difference distribution, i.e., Distri(·) as the distribution values
of the non-leaf nodes. Algorithm 1 outlines the process for
computing the distribution score Distri(·).
Summary score: For two summary sets S1, S2 ⊆V , the sim-
ilarity summary score of S1 and difference summary score of
S2 on y ∈V are denoted as simSmyS1(y) and difSmyS2(y)
as follows, representing the maximum similarity and difference
impact on y among all representative elements in S1 and S2.
simSmyS1(y) =
max
x∈S1∩anc(y) simRepx(y) · (1 −Distri(x))
difSmyS2(y) =
max
x∈S2∩anc(y) difRepx(y) · Distri(x)



## Page 4

4876
IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING, VOL. 37, NO. 8, AUGUST 2025
Fig. 2.
An example of passing up the similarity and difference distribution. Here β = 1. Finally, the root r has SimD(r) = [50, 45] and DifD(r) = [100, 0].
Algorithm 1: Computing Distri(x).
Input:A non-leaf node x ∈V, two weighted trees T1, T2.
Output:Distri(x) ∈[0, 1].
1: Let Distri(x) ←0;
2: SimD(x) ←
[SimT1
1 (x), SimT2
1 (x), . . ., SimT1
β (x), SimT2
β (x)];
3: DifD(x) ←
[Dif T1
1 (x), Dif T2
1 (x), . . ., Dif T1
β (x), Dif T2
β (x)];
4: sumSimD(x) ←
1≤i≤β,1≤j≤2 SimTj
i (x);
5: sumDifD(x) ←
1≤i≤β,1≤j≤2 Dif Tj
i (x);
6: SimD(x) ←SimD(x)/sumSimD(x);
7: DifD(x) ←DifD(x)/sumDifD(x);
8: for i = 1 to β do
9:
for j = 1 to 2 do
10:
Distri(x) ←
Distri(x) + (

Dif Tj
i (x) −

SimTj
i (x))2;
11: Distri(x) ←
1
√
2

Distri(x);
12: return Distri(x);
Based on the deﬁnition of simSmyS1(x) and difSmyS2(x),
the summary score of the set S is deﬁned as:
sum(S) =

y∈V
simSmyS1(y) +

y∈V
difSmyS2(y)
B. Property Analysis
Submodularity: Given a similarity summary node x ∈S1,
let the set of nodes that take x as their similarity summary
node, denoted by θS1(x) = {y ∈dec(x) : simSmyS1(y) =
simRepx(y) · (1 −Distri(x))}. Similarly, for a difference
summary node x ∈S2, the set of nodes that take x as their
difference summary node is deﬁned as: θS2(x) = {y ∈dec(x) :
difSmyS2(y) = difRepx(y) · Distri(x)}.
Theorem 1:
sum is submodular, i.e., for all sets Sa ⊂
Sb ⊂V, and element x ∈V \ Sb, we have sum(Sa ∪{x}) −
sum(Sa) ≥sum(Sb ∪{x}) −sum(Sb).
Proof:
To prove sum is submodular, we ﬁrst prove the
submodularity of S1, and then extend it to S2, concluding that
sum is submodular. Given a set S1 ⊂T1 ⊂V for representing
similarity, ∀x ∈V \ T1 can be added to the set S1 or T1. There-
fore, T ′
1 = T1 ∪{x} and S′
1 = S1 ∪{x}.
Algorithm 2: SVDT(S1, S2, k).
Input:Two weighted trees T1, T2 = {V, E}, a positive
integer k.
Output:A set of k1 similarity summary elements S1, and a
set of k2 difference summary elements S2.
1: Let S ←∅, S1 ←∅, S2 ←∅;
2: Compute initial score Distri(x) for all non-leaf nodes
satisfying x ∈V by Algorithm 1;
3: while |S1| + |S2| < k do
4:
x′ ←arg maxx∈V\S(sum(S ∪{x}) −sum(S));
5:
S ←S ∪{x′};
6:
if x′ provides higher marginal gain in similarity than
difference then
7:
S1 ←S1 ∪{x′};
8:
else
9:
S2 ←S2 ∪{x′};
10: return S1, S2;
Firstly,
∀y ∈V, simSmyS1(y) ≤simSmyT1(y)
and
simSmyS′
1(y) ≤simSmyT ′
1(y) are obvious. For ∀y ∈θT ′
1(x),
from above, simRepx(y) · (1 −Distri(x)) = simSmyT ′
1(y)
≥simSmyS′
1(y), and since x ∈S′
1, we also have simRepx
(y) · (1 −Distri(x)) ≤simSmyS′
1(y). Thus, simRepx(y) ·
(1 −Distri(x)) = simSmyS′
1(y),
implying
y ∈θS′
1(x).
Therefore, θT ′
1(x) ⊆θS′
1(x). So we have sum(T ′
1) −sum(T1)
= 
y∈V(simSmyT ′
1(y) −simSmyT1(y)) = 
y∈θT ′
1(x)(sim
Repx(y) · (1 −Distri(x)) −simSmyT1(y)). Similarly, sum
(S′
1) −sum(S1)=
y∈θS′
1(x)(simRepx(y) · (1 −Distri(x))
−simSmyS1(y)). Thus, we can obtain 
y∈θS′
1(x)(sim
Repx(y) · (1 −Distri(x)) −simSmyS1(y)) ≥
y∈θT ′
1(x)
(simRepx(y) · (1 −Distri(x)) −simSmyT1(y)), leading to
sum(S′
1) −sum(S1) ≥sum(T ′
1) −sum(T1).
For the set S2 representing difference, the proof follows as
that in S1. The distinction lies in the deﬁnition of similarity and
difference summary scores, simSmyS1(y) = maxx∈S1∩anc(y)
simRepx(y) · (1 −Distri(x)),
and
difSmyS2(y) =
maxx∈S2∩anc(y) difRepx(y) · Distri(x). Since Distri(x) ∈
[0, 1], the submodularity property also holds for set S2. Thus,
sum(S′) −sum(S) ≥sum(T ′) −sum(T).
□
Approximation: InTheorem1, weestablishthesubmodularity
of the summary score function sum. Thus, a greedy algorithm



## Page 5

CHEN et al.: TOP-K REPRESENTATIVE SEARCH FOR COMPARATIVE TREE SUMMARIZATION
4877
Fig. 3.
Summary visualization based on SVDT answers.
Fig. 4.
Handle two trees’ summarization in different structures.
can be developed to achieve (1 −1/e)-approximation for max-
imizing a monotone submodular set function with a cardinality
constraint [13].
C. Greedy Algorithm SVDT for Differential Summarization
Algorithm 2 outlines the details of the SVDT algorithm. For
any summary set S ⊂V and any candidate x ∈V \ S, we com-
pute the gain Δsum(x|S) = sum(S ∪{x}) −sum(S) ≥0.
First, we compute Distri(x) for all non-leaf nodes x using
Algorithm 1 (line 2). When |S1| + |S2| < k, it takes the element
x′ thatcanmakethemaximalmarginalgainonthesetS,andadds
x′ to the set S (lines 3-5). If x′ contributes a greater marginal gain
in representing similarity than the difference, it is added to set S1
(lines 6-7); Otherwise, it is added to set S2 (lines 8-9). Finally,
the algorithm returns the similarity set S1 and the difference set
S2 (line 10).
D. Summary Visual Representation
We make the summary visual representation based on SVDT
answer S. Consider a hierarchical tree T in Fig. 3(a) and k = 7.
Four nodes in the set S1 contributing to similarity are in red,
while three nodes in the set S2 contributing to difference are in
blue. T is an instance subtree of real ACM CCS hierarchical tree
in Fig. 10(a). To achieve a compact visualization, we take two
steps. Firstly, for nodes that are neither colored themselves nor
have colored descendants, we prune them and their descendants.
The remaining nodes form the topology structure as shown in
Fig. 3(b). Secondly, we skip non-representative nodes in chains
of representative nodes with ancestor-descendant relationships.
For instance, in the chains {I1, I6, I13} and {I1, I6, I14}, we
only show the ancestor-descendant relationships from I1 to I13
and from I1 to I14. In such cases, we represent their connection
with dashed lines in the summary visual representation T ∗as
shown in Fig. 3(c).
E. Discussion of Handling Two Trees With Different Structures
Since comparisons between trees with different structures are
also widely exist in practical situations, we discuss the solution
in Fig. 4. Speciﬁcally, we compare the structural differences
between two trees T1 and T2, and then introduce new edges
and nodes at the corresponding positions. These newly added
nodes are assigned a weight of 0, enabling the transformation
of the trees into a uniﬁed structure for subsequent similarity and
difference comparisons.
V. EXPERIMENTS
In this section, we conducted extensive experiments to eval-
uate the performance. The source code of our algorithm is
available at https://github.com/csyqchen/TKDE_SVDT.
Datasets: We used three pairs of real-world datasets contain-
ing hierarchical terminologies. Latt&Lnur are extracted from
the Medical Entity Dictionary [1] with 4226 entities in a tree
height of 22, which consists of information on patient and nurse
access to online knowledge resources. The Anime hierarchical
structure, extracted from the “Anime” directory in Wikipedia,
includes 15,135 animes and their frequency represented by the
number of page views in Jan 2018 and Jan 2024 [15]. The
Yago hierarchical structure is an extracted tree of ontology
structure yagoTaxonomy with 493,839 taxonomies in multilin-
gual Wikipedias, which are by randomly assigning two different
weights denoted as Yago1 and Yago2.
Methods Comparison: To evaluate the quality of our method
SVDT, we compare it with three baseline algorithms, including
GVDO [5], FEQ [1], and CAGG [1]. GVDO is a summarization
approach applied to ontology-based structure. FEQ is a method
of selecting k nodes with the highest frequency as the summa-
rized answer. CAGG selects k nodes with the highest frequency
as the summarization answer by controlling descendant contri-
bution. Note that these three competitor methods are designed to
work on a single tree. For comparison, we implement variants of
methods running on a a common tree, which takes the minimum
weight of a node in two trees T1 and T2 as the new weight in
this common tree. In addition, we set the parameters k = 10 and
β = 50 for SVDT by default.
Evaluation Metrics: To evaluate the quality of summarization
answers, we use three metrics: the diversity Div(S), the query
closeness CQ(S) [4], and average level difference Ald(S) [5].
First, Div(S) computes the diversity of the original data set
represented by the summary node in two trees T1, T2. The higher
the diversity, the better the summary.
Div(S) =

x∈S∩anc(y)
|freqT1(y) −freqT2(y)| · disx(y)
Second, we design a query closeness CQ(S) to test the summary
S’s distance to query Q. We randomly selected 500 vertices Q.
For each vertex q ∈Q, we accumulates the sum of the minimum
distance from q to S. A lower CQ(S) indicates a superior
summary.
CQ(S) =

q∈Q
min
x∈S distT (q, x)
Third, the average level difference Ald(S) is deﬁned as the
average level difference between summary node and weighted
node, denoted by the following formula. A smaller average
level difference means that the summary graph more effectively



## Page 6

4878
IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING, VOL. 37, NO. 8, AUGUST 2025
Fig. 5.
Diversity Div(S) evaluation on all datasets.
Fig. 6.
Query closeness CQ(S) evaluation on all datasets.
Fig. 7.
Average level difference Ald(S) evaluation on all datasets.
preserves the hierarchical structure of the original graph.
Ald(S) =

y∈V
min
x∈S∩anc(y)(level(y) −level(x)) · α(x, y)

y∈V α(x, y)
Here level(x) = distT (x, r0) in tree T rooted by r0 and
α(x, y) = |freqT1(y) −freqT2(y)|.
Exp-I: Quality Evaluation: Fig. 5 demonstrates that SVDT
markedly surpasses three baseline methods in capturing diver-
sity Div(S), thereby indicating its superiority in summarizing
intrinsic tree relationships. Figs. 6 and 7 both illustrate that our
algorithm, SVDT, maintains the closest distance and the smallest
average level difference in almost all datasets compared to other
baseline methods. This demonstrates that our summary is the
most effective in closely mirroring the original tree structure of
the dataset.
Exp-II: Scalability Test: We generated four synthetic datasets
with tree node sizes from 103 to 106. In all experiments, we
ﬁxed k = 10 and β = 3 to compare the scalability of SVDT. The
baseline in Fig. 8 is a summary approach that ﬁnds the optimal
combination of S1 and S2. As the tree node size increases,
SVDT exhibits remarkable scalability and efﬁciency, reﬂecting
the effectiveness of Algorithm 2.
Exp-III: Case Study on ACM CCS Topic Summarization:
Fig. 10(a) illustrates publication counts of research papers in dif-
ferent ﬁve-year periods on a poly-hierarchical ontology (ACM
Computing Classiﬁcation System [14]). Queries for topics (I0,
Fig. 8.
Scalability test on four synthetic datasets.
Fig. 9.
Usability evaluation on ACM CCS topic summarization.
Fig. 10.
Case study on ACM CCS hierarchical trees.
I1,..., I16) in blue, with speciﬁc query term names in black
and the corresponding research paper publication counts in red.
For k = 7, in Fig. 10(b), we show the summarization given by
GVDO with the best experimental results among all baselines in
qualityevaluation.GVDOsummarizesattractivetopicsbutlacks
priority or changes, providing limited information to users. In
contrast, our SVDT summarization in Fig. 10(c) has red and blue
themes, representing similarities and differences, respectively.
For the four second-level topics (I1, I2, I3, I4) in the original
graph, SVDT uses varying shades of red to indicate the popu-
larity levels of these topics. Additionally, we show the diversity
by highlighting the changes in some topics between the two
ﬁve-year periods. Nodes (I5, I13, I14) are colored with different
shades of blue, and their direct ancestor computing methodology
is marked with the deepest shade of red. These show that the
popularity of artiﬁcial intelligence, learning paradigms, and
machine learning approaches has changed signiﬁcantly in ﬁve
years and is showing a trend of increasing popularity.
Exp-IV: Usability Study on ACM CCS Topic Summarization:
We conduct usability evaluation for top-k topic summariza
tion, selecting k topics from Fig. 10(a) to capture commonalities
and trends over different ﬁve-year periods. We set k = 7 and
invite 10 users with the background in computer science and aca-
demic research to choose their top-7 topics for summarization.



## Page 7

CHEN et al.: TOP-K REPRESENTATIVE SEARCH FOR COMPARATIVE TREE SUMMARIZATION
4879
Then, we compare their selections with different methods (FEQ,
GVDO, CAGG, and SVDT). As shown in Fig. 9, our method
achieves an average matching accuracy of 85.7%, signiﬁcantly
outperforming the 60% accuracy by other methods. This result
highlights the effectiveness of our algorithm in homogeneous
and differential summarization.
VI. CONCLUSION
In this paper, we introduce the kVDT problem aimed at
visually summarizing two weighted hierarchical trees of iden-
tical structure. The SVDT algorithm selects k representative
nodes, summarizing the commonalities and diversities between
two weighted trees. We propose a distribution normalization
technique extending Hellinger distance for efﬁcient non-leaf
node computation. Our method includes a summary visual rep-
resentationfor thecompact visualization. Extensiveexperiments
demonstrate the superiority of our proposed algorithm.
REFERENCES
[1] X. Jing and J. J. Cimino, “Graphical methods for reducing, visualizing and
analyzing large data sets using hierarchical terminologies,” in Proc. AMIA
Annu. Symp., 2011, pp. 635.
[2] E. M. Jin, M. Girvan, and M. E. J. Newman, “Structure of growing social
networks,” Phys. Rev. E, vol. 64, no. 4, 2001, Art. no. 046132.
[3] D. Koutra, A. Parikh, A. Ramdas, and J. Xiang, “Algorithms for graph
similarity and subgraph matching,” in Proc. Ecol. Inference Conf., 2011,
Art. no. 50.
[4] X. Huang, B. Choi, J. Xu, W. K. Cheung, Y. Zhang, and J. Liu, “Ontology-
based graph visualization for summarized view,” in Proc. 2017 ACM Conf.
Inf. Knowl. Manage., 2017, pp. 2115–2118.
[5] X. Zhu et al., “Efﬁcient and optimal algorithms for tree summarization
with weighted terminologies,” IEEE Trans. Knowl. Data Eng., vol. 35,
no. 3, pp. 2500–2514, Mar. 2023.
[6] D. Chu, F. Zhang, W. Zhang, Y. Zhang, and X. Lin, “Graph summarization:
Compactness meets efﬁciency,” in Proc. ACM Manage. Data, vol. 2, no. 3,
pp. 1–26, 2024.
[7] A. Kim, L. V. S. Lakshmanan, and D. Srivastava, “Summarizing hierar-
chical multidimensional data,” in Proc. IEEE 36th Int. Conf. Data Eng.,
2020, pp. 877–888.
[8] S. Navlakha, R. Rastogi, and N. Shrivastava, “Graph summarization with
bounded error,” in Proc. 2008 ACM SIGMOD Int. Conf. Manage. Data,
2008, pp. 419–432.
[9] K. Lee, J. Ko, and K. Shin, “Slugger: Lossless hierarchical summarization
of massive graphs,” in Proc. IEEE 38th Int. Conf. Data Eng., 2022,
pp. 472–484.
[10] Y. Wu, Z. Zhong, W. Xiong, and N. Jing, “Graph summarization for
attributed graphs,” in Proc. 2014 Int. Conf. Inf. Sci., Electron. Electr. Eng.,
2014, pp. 503–507.
[11] K. A. Kumar and P. Efstathopoulos, “Utility-driven graph summarization,”
in Proc. VLDB Endowment, vol. 12, no. 4, pp. 335–347, 2018.
[12] E. Hellinger, “Neue begrùndung der theorie quadratischer formen von un-
endlichvielen veránderlichen,” J. Reine Angew. Math., vol. 1909, no. 136,
pp. 210–271, 1909.
[13] G. L. Nemhauser, L. A. Wolsey, and M. L. Fisher, “An analysis of ap-
proximations for maximizing submodular set functions—I,” Math. Prog.,
vol. 14, pp. 265–294, 1978.
[14] Apr. 2025. [Online]. Available: https://dl.acm.org/ccs
[15] Apr. 2025. [Online]. Available: https://pageviews.wmcloud.org
Yuqi Chen received the master’s degree from Hong
Kong Baptist University in 2023. She is currently a
researchassistantwithHongKongBaptistUniversity.
Her research interests include graph data manage-
ment and mining.
XinHuangreceivedthePhDdegreefromtheChinese
University of Hong Kong in 2014. He is currently an
associate professor with Hong Kong Baptist Univer-
sity. His research interests mainly include focus on
graph data management and mining.
Bilian Chen received the PhD degree from the Chi-
nese University of Hong Kong in 2012. Currently,
she is an associate professor with Xiamen University.
Her research interests include machine learning, op-
timization theory and recommendation system. Her
publications appear in IEEE Transactions on Neural
Networks and Learning Systems, SIAM Journal on
Optimization, Journal of Global Optimization, Infor-
mation Sciences, and so on.


