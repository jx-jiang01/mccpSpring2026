
## Page 1

Effective Community Search for Large Attributed Graphs
Yixiang Fang, Reynold Cheng, Siqiang Luo, Jiafeng Hu
Department of Computer Science, The University of Hong Kong, Pokfulam Road, Hong Kong
{yxfang, ckcheng, sqluo, jhu}@cs.hku.hk
ABSTRACT
Given a graph G and a vertex q ∈G, the community search query
returns a subgraph of G that contains vertices related to q. Commu-
nities, which are prevalent in attributed graphs such as social net-
works and knowledge bases, can be used in emerging applications
such as product advertisement and setting up of social events. In
this paper, we investigate the attributed community query (or AC-
Q), which returns an attributed community (AC) for an attributed
graph. The AC is a subgraph of G, which satisﬁes both structure
cohesiveness (i.e., its vertices are tightly connected) and keyword
cohesiveness (i.e., its vertices share common keywords). The AC
enables a better understanding of how and why a community is
formed (e.g., members of an AC have a common interest in mu-
sic, because they all have the same keyword “music”). An AC can
be “personalized”; for example, an ACQ user may specify that an
AC returned should be related to some speciﬁc keywords like “re-
search” and “sports”.
To enable efﬁcient AC search, we develop the CL-tree structure
and three algorithms based on it. We evaluate our solutions on four
large graphs, namely Flickr, DBLP, Tencent, and DBpedia. Our re-
sults show that ACs are more effective and efﬁcient than existing
community retrieval approaches. Moreover, an AC contains more
precise and personalized information than that of existing commu-
nity search and detection methods.
1.
INTRODUCTION
Due to the recent developments of gigantic social networks (e.g.,
Flickr, Facebook, and Twitter), the topic of attributed graphs has
attracted attention from industry and research communities [28, 3,
6, 15, 17, 32, 18]. An attributed graph is essentially a graph associ-
ated with text strings or keywords. Figure 1 illustrates an attributed
graph, where each vertex represents a social network user, and its
keywords describe the interest of that user.
In this paper, we investigate the attributed community query (or
ACQ). Given an attributed graph G and a vertex q ∈G, the ACQ
returns one or more subgraphs of G known as attributed commu-
nities (or ACs). An AC is a kind of community, which consists of
vertices that are closely related [27, 5, 4, 16, 23, 12]. Particularly,
Bob:{research, sports, yoga}
Tom:{fiction, film, game}
Alice:{art, music, yoga}
Jack:{research, sports, tour}
Mike:{film, research, sports}
Anna:{art, cook, music}
Ada:{art, cook, music}
John:{research, sports, web}
Alex:{chess, tour, research}
Figure 1: Attributed graph and AC (circled).
Table 1: Classiﬁcation of works in community retrieval.
Graph
Type
Community
detection (CD)
Community
search (CS)
Non-attributed
[23, 12]
[27, 5, 4, 16, 19]
Attributed
[33, 22, 21, 28, 24]
ACQ (This paper)
an AC satisﬁes structure cohesiveness (i.e., its vertices are close-
ly linked to each other) and keyword cohesiveness (i.e., its vertices
have keywords in common). Figure 1 illustrates an AC (circled),
which is a connected subgraph with vertex degree 3; its vertices
{Jack, Bob, John, Mike} have two keywords (i.e., “research”
and “sports”) in common.
Prior works. The problems related to retrieving communities
from a graph can generally be classiﬁed into community detection
(CD) and community search (CS). In general, CD algorithms aim
to retrieve all communities for a graph [33, 22, 21, 28, 24]. These
solutions are not “query-based”, i.e., they are not customized for a
query request (e.g., a user-speciﬁed query vertex). Moreover, they
can take a long time to ﬁnd all the communities for a large graph,
and so they are not suitable for quick or online retrieval of commu-
nities. To solve these problems, CS solutions have been recently
developed [27, 5, 4, 16]. These approaches are query-based, and
are able to derive communities in an “online” manner. However,
existing CS algorithms assume non-attributed graphs, and only use
the graph structure information to ﬁnd communities. The ACQ is a
class of CS problem for attributed graphs. As we will show, the use
of keyword information can signiﬁcantly improve the effectiveness
of the communities retrieved. Table 1 summarizes some represen-
tative existing works in this area.
Features of ACs. We now present more details about ACs.
• Ease of interpretation. As demonstrated in Figure 1, an AC
contains tightly-connected vertices with similar contexts or back-
grounds. Thus, an ACQ user can focus on the common keywords
or features of these vertices (e.g., the vertices of the AC in this ex-
ample contain “research” and “sports”, reﬂecting that all members
of this AC like research and sports). We call the set of common
1
 HKU CS Tech Report TR-2016-01



## Page 2

keywords among AC vertices the AC-label. In our experiments, the
AC-labels facilitate understanding of the vertices that form the AC.
The design of ACs allows it to be used in setting up of social
events. For example, if a Twitter member has many keywords about
traveling (e.g., he posted a lot of photos about his trips, with key-
words), issuing an ACQ with this member as the query vertex may
return other members interested in traveling, because their vertices
also have keywords related to traveling. A group tour can then be
recommended to these members.
• Personalization. The user of an ACQ can control the semantic-
s of the AC, by specifying a set of S of keywords. Intuitively, S
decides the meaning of the AC based on the user’s need. If we let
q=Jack and S={“research”}, the AC is formed by {Jack, Bob,
John, Mike, Alex}, who are all interested in research. Let us
consider another example in the DBLP bibliographical network,
where each vertex’s attribute is represented by the top-20 frequent
keywords in their publications. Let q=Jim Gray. If S is the set
of keywords {transaction, data, management, system, research},
we obtain the AC in Figure 2(a), which contains six prominen-
t database researchers closely related to Jim. On the other hand,
when S is {sloan, digital, sky, survey, SDSS}, the ACQ yield-
s another AC in Figure 2(b), which indicates the seven scientists
involved in the SDSS project 1. Thus, with the use of different key-
word sets S, different “personalized” communities can be obtained.
Existing CS algorithms, which do not handle attributed graphs,
may not produce the two ACs above. For example, the CS algorith-
m in [27] returns the community with all the 14 vertices shown in
Figures 2(a) and (b). The main reasons are: (1) these vertices are
heavily linked with Jim; and (2) the keywords are not considered.
In contrast, the use of set S in the ACQ places these vertices into
two communities, containing vertices that are cohesive in terms of
structure and keyword. This allows a user to focus on the important
vertices that are related to S. For example, using the AC of Fig-
ure 2(a), a database conference organizer can invite speakers who
have a close relationship with Jim.
The personalization feature is also useful in marketing. Suppose
that Mary, a yoga lover, is a customer of a gym. An ACQ can
be issued on a social network, with Mary as the query vertex and
S={“yoga”}. Since members of the AC contain the keyword “yo-
ga”, they can be the gym’s advertising targets. On the other hand,
current CS algorithms may return a community that contains one or
more vertices without the keyword “yoga”. It is not clear whether
the corresponding user of this vertex is interested in yoga.
• Online evaluation. Similar to other CS solutions, we have devel-
oped efﬁcient ACQ algorithms for large graphs, allowing ACs to be
generated quickly upon a query request. On the contrary, existing
CD algorithms [33, 24, 22, 21] that generate all communities for
a graph are often considered to be ofﬂine solutions, since they are
often costly and time-consuming, especially on very large graphs.
Technical challenges and our contributions. We face two im-
portant questions: (1) What should be a sound deﬁnition of an AC?
(2) How to evaluate ACQ efﬁciently? For the ﬁrst question, we de-
ﬁne an AC based on the minimum degree, which is one of the most
common structure cohesiveness metrics [23, 12, 27, 5]. This mea-
sure requires that every vertex in the community has a degree of k
or more. We formulate the keyword cohesiveness as maximizing
the number of shared keywords in keyword set S. The shared key-
words naturally reveal the common features among vertices (e.g.,
common interest of social network users). We can also use these
shared keywords to explain how a community is formed.
1URL of the SDSS project: http://www.sdss.org.
Jim Gray
Michael Stonebraker
Hector Garcia-Moina
Stanley B. Zdonik
Gerhard Weikum
Bruce G. Lindsay
Michael L. Brodie
(a) S={transaction, data, man-
agement, system, research}
Jim Gray
Peter Z. Kunszt
Christopher Stoughton
Alexander S. Szalay
Jordan Raddick
Jan Vandenberg
Ani Thakar
Tanu Malik
(b) S={sloan, digital, sky, da-
ta, sdss}
Figure 2: Two ACs of Jim Gray.
The second question is not easy to answer, because the attribut-
ed graph G to be explored can be very large, and the (structure and
keyword) cohesiveness criteria can be complex to handle. A simple
way is ﬁrst to consider all the possible keyword combinations, and
then return the subgraphs, which satisfy the minimum degree con-
straint and have the most shared keywords. This solution, which
requires the enumeration of all the subsets of q’s keyword set, has
a complexity exponential to the size l of q’s keyword set. In our
experiments, for some queries, l can be up to 30, resulting in the
consideration of 230 = 1, 073, 741, 824 subsets of q. The algorith-
m is impractical, especially when q’s keyword set is large.
We observe the anti-monotonicity property, which states that giv-
en a set S of keywords, if it appears in every vertex of an AC, then
for every subset S′ of S, there exists an AC in which every vertex
contains S′. We use this intuition to propose better algorithms. We
further develop the CL-tree, an index that organizes the vertex key-
word data in a hierarchical structure. The CL-tree has a space and
construction time complexity linear to the size of G. We have de-
veloped three different ACQ algorithms based on the CL-tree, and
they are able to achieve a superior performance.
We have performed extensive experiments on four large real graph
datasets (namely Flickr, DBLP, Tencent, and DBpedia). We found
that a large number of common keywords appear across vertices in
our graph datasets. In DBLP, for instance, an AC with one com-
mon keyword contains over 5,000 vertices on average; an AC with
two common keywords contains over 700 vertices. Hence, using
shared keywords among vertices as keyword cohesiveness makes
sense. We have also studied how to quantify the quality of a com-
munity, based on occurrence frequencies of keywords and similar-
ity between the keyword sets of two vertices. We conducted a de-
tailed case study on DBLP. These results conﬁrm the superiority of
the AC over the communities returned by existing community de-
tection and community search algorithms, in terms of community
quality. The performance of our best algorithm is 2 to 3 order-of-
magnitude better than solutions that do not use the CL-tree. An-
other advantage of our approaches is that they organize and search
vertex keywords for ACs effectively, achieving a higher efﬁciency
than existing community search solutions (that do not use vertex
keywords in the community search process).
Organization. We review the related work in Section 2, and
deﬁne the ACQ problem formally in Section 3. Section 4 presents
the basic solutions, and Section 5 discusses the CL-tree index. We
present the query algorithms in Section 6. Our experimental results
are reported in Section 7. We conclude in Section 8.
2.
RELATED WORK
Community detection (CD). A large class of studies aim to dis-
cover or detect all the communities from an entire graph. Table 1
summarises these works. Earlier solutions, such as [23, 12], em-
ploy link-based analysis to obtain these communities. However,
they do not consider the textual information associated with graphs.
2



## Page 3

Recent works focus on attributed graphs, and use clustering tech-
niques to identify communities. For instance, Zhou et al. [33] con-
sidered both links and keywords of vertices to compute the vertices’
pairwise similarities, and then clustered the graph. Ruan et al. [24]
proposed a method called CODICIL. This solution augments the
original graphs by creating new edges based on content similarity,
and then uses an effective graph sampling to boost the efﬁciency of
clustering. We will compare ACQ with this method experimentally.
Another common approach is based on topic models. In [22,
21], the Link-PLSA-LDA and Topic-Link LDA models joint-
ly model vertices’ content and links based on the LDA model. In [28],
the attributed graph is clustered based on probabilistic inference.
In [25], the topics, interaction types and the social connections
are considered for discovering communities. CESNA [30] detect-
s overlapping communities by assuming communities “generate”
both the link and content. A discriminative approach [31] has also
been considered for community detection. As discussed before, CD
algorithms are generally slow, as they often consider the pairwise
distance/similarity among vertices. Also, it is not clear how they
can be adapted to perform online ACQ. In this paper, we propose
online algorithms for ﬁnding communities on attributed graphs.
Community search (CS). Another class of solutions aims to ob-
tain communities in an “online” manner, based on a query request.
For example, given a vertex q, several existing works [27, 5, 19,
4, 16] have developed fast algorithms to obtain a community for q.
To measure the structure cohesiveness of a community, the mini-
mum degree is often used [27, 5, 19]. Sozio et al. [27] proposed
the ﬁrst algorithm Global to ﬁnd the k- d
core containing q. Cui
et al. [5] proposed Local, which uses local expansion techniques
to enhance the performance of Global. We will compare these
two solutions in our experiments. Other deﬁnitions, including k-
clique [4] and k-truss [16], have also been considered for searching
communities. A recent work [19] ﬁnds communities with high in-
ﬂuence. These works assume non-attributed graphs, and overlook
the rich information of vertices that come with attributed graphs.
As we will see, performing CS on attributed graphs is better than
on non-attributed graphs.
Graph keyword search. Given an attributed graph G and a set
Q of keywords, graph keyword search solutions output a tree struc-
ture, whose nodes are vertices of G, and the union of these vertices’
keyword sets is a superset of Q [3, 6, 17]. Recent work studies the
use of a subgraph of G as the query output [18]. These works
are substantially different from the ACQ problem. First, they do
not specify query vertices as required by the ACQ problem. Sec-
ond, the tree or subgraph produced do not guarantee structure co-
hesiveness. Third, keyword cohesiveness is not ensured; there is no
mechanism that enforces query keywords to be shared among the
keyword sets of all query output’s vertices. Thus, graph keyword
search solutions are not designed to ﬁnd ACs.
Graph pattern matching (GPM). Given a pattern P, the goal
of GPM is to extract a set R of subgraphs of G, where for every
r ∈R, r is highly similar to P. Tong et al. [8] studied the use of
lines, loops and stars; Fan et al. [9, 10] proposed bounded simula-
tion techniques for GPM queries; in [11], GPM has been studied
for ﬁnding association rules from graphs. However, there is no de-
tailed study about how to use GPM for community search. To do
this, a user has to deﬁne P, but this is not trivial: there are many
possible topologies for P, and numerous ways of placing keyword-
s on the vertices in P. Moreover, current GPM solutions focus on
small patterns that generate small communities, and it is not clear
whether they can support large and complex ones. Answering AC-
Q with GPM can also be expensive, since it involves enumerating
many patterns and ﬁnding an AC with the largest number of shared
Table 2: Symbols and meanings.
Symbol
Meaning
G(V, E)
An attributed graph with vertex set V and edge set E
W(v)
The keyword set of vertex v
degG(v)
The degree of vertex v in G
G[S′]
The largest connected subgraph of G s.t. q ∈G[S′],
and for any v ∈G[S′], S′ ⊆W(v)
Gk[S′]
The largest connected subgraph of G s.t. q ∈Gk[S′],
and for any v ∈Gk[S′], degGk[S′]v ≥k and S′ ⊆W(v)
keywords. For the ACQ problem, there is no need to specify P.
3.
THE ACQ PROBLEM
We now discuss the attributed graph model, the k-core, and the
AC. In the CS and CD literature, most existing works assume that
the underlying graph is undirected [27, 19, 28, 24]. We also sup-
pose that an attributed graph G(V, E) is undirected, with vertex set
V and edge set E. Each vertex v ∈V is associated with a set of
keywords, W(v). Let n and m be the corresponding sizes of V and
E. The degree of a vertex v of G is denoted by degG(v). Table 2
lists the symbols used in the paper.
A community is often a subgraph of G that satisﬁes structure co-
hesiveness (i.e., the vertices contained in the community are linked
to each other in some way). A common notion of structure cohe-
siveness is that the minimum degree of all the vertices that appear
in the community has to be k or more [27, 26, 2, 7, 5, 19]. This is
used in the k-core and the AC. Let us discuss the k-core ﬁrst.
DEFINITION 1
(k-CORE [26, 2]). Given an integer k (k ≥
0), the k-core of G, denoted by Hk, is the largest subgraph of G,
such that ∀v ∈Hk, degHk(v) ≥k.
We say that Hk has an order of k. Notice that Hk may not be
a connected graph [2], and its connected components, denoted by
k- d
cores, are usually the “communities” returned by k- d
core search
algorithms.
A:{w, x, y}
D:{x, y, z}
B:{x}
C:{x, y}
F:{y}
E:{y, z}
G:{x, y}
J:{x}
I:{x}
H:{y, z}
1
2
3
(a) graph
Core number
Vertices
0
J
1
F, G, H, I
2
E
3
A, B, C, D
(b) core number
Figure 3: Illustrating the k-core and the AC.
EXAMPLE 1. In Figure 3(a), {A, B, C, D} is both a 3-core
and a 3- d
core. The 1-core has vertices {A, B, C, D, E, F, G, H, I},
and is composed of two 1- d
core components: {A, B, C, D, E, F, G}
and {H, I}. The number k in each circle represents the k- d
core
contained in that ellipse.
Observe that k-cores are “nested” [2]: given two positive in-
tegers i and j, if i < j, then Hj ⊆Hi. In Figure 3(a), H3 is
contained in H2, which is nested within H1.
DEFINITION 2
(CORE NUMBER). Given a vertex v ∈V , its
core number, denoted by coreG[v], is the highest order of a k-core
that contains v.
3



## Page 4

A list of core numbers and their respective vertices for Example 1
are shown in Figure 3(b). In [2], an O(m) algorithm was proposed
to compute the core number of every vertex.
We now formally deﬁne the ACQ problem as follows.
PROBLEM 1
(ACQ). Given a graph G(V, E), a positive in-
teger k, a vertex q ∈V and a set of keywords S ⊆W(q), return a
set G of graphs, such that ∀Gq ∈G, the following properties hold:
• Connectivity. Gq ⊆G is connected and contains q;
• Structure cohesiveness. ∀v ∈Gq, degGq(v) ≥k;
• Keyword cohesiveness. The size of L(Gq, S) is maximal, where
L(Gq, S) = ∩v∈Gq(W(v) ∩S) is the set of keywords shared in S
by all vertices of Gq.
We call Gq the attributed community (or AC) of q, and L(Gq, S)
the AC-label of Gq. In Problem 1, the ﬁrst two properties are also
speciﬁed by the k- d
core of a given vertex q [27]. The keyword co-
hesiveness (Property 3), which is unique to Problem 1, enables the
retrieval of communities whose vertices have common keyword-
s in S. We use S to impose semantics on the AC produced by
Problem 1. By default, S = W(q), which means that the AC gen-
erated should have keywords common to those associated with q.
If S ⊂W(q), it means that the ACQ user is interested in forming
communities that are related to some (but not all) of the keywords
of q. A user interface could be developed to display W(q) to the
user, allowing her to include the desired keywords into S. For ex-
ample, in Figure 3(a), if q=A, k=2 and S={w, x, y}, the output of
Problem 1 is {A, C, D}, with AC-label {x, y}, meaning that these
vertices share the keywords x and y.
We require L(Gq, S) to be maximal in Property 3, because we
wish the AC(s) returned only contain(s) the most related vertices,
in terms of the number of common keywords. Let us use Fig-
ure 3(a) to explain why this is important. Using the same query
(q=A,k=2,S= {w, x, y}), without the “maximal” requirement, we
can obtain communities such as {A, B, E} (which do not share any
keywords), {A, B, D}, or {A, B, C} (which share 1 keyword).
Note that there does not exist an AC with AC-label being exact-
ly {w, x, y}. Our experiments (Section 7) show that imposing the
“maximal” constraint yields the best result. Thus, we adopt Prop-
erty 3 in Problem 1. If there is no AC whose vertices share one or
more keywords (i.e., |L(Gq, S)|=0), we return the subgraph of G
that satisﬁes Properties 1 and 2 only.
2
There are other candidates for structure cohesiveness (e.g., k-
truss, k-clique) and keyword cohesiveness (e.g., Jaccard similarity
and string edit distance). In our report [29], we studied a variant
of keyword cohesiveness, in which an ACQ user may specify that
an AC returned must contain vertices having speciﬁc keywords.
We also examined its approximate version, where given a threshold
θ ∈[0, 1], each vertex in an AC has at least |S| × θ keywords in S.
These variants can be easily supported by our solutions to ACQ. An
interesting future work is to compare the use of different structure
and keyword cohesiveness deﬁnitions in an ACQ.
4.
BASIC SOLUTIONS
For ease of presentation, we say that v contains a set S′ of key-
words, if S′ ⊆W(v). We use G[S′] to denote the largest connect-
ed subgraph of G, where each vertex contains S′ and q ∈G[S].
We use Gk[S′] to denote the largest connected subgraph of G[S′],
in which every vertex has degree being at least k in Gk[S′]. We
call S′ a qualiﬁed keyword set for the query vertex q on the graph
G, if Gk[S′] exists.
2In practice, the query user can be alerted by the system when there
is no sharing among the vertices.
Given a query vertex q, a straightforward method to answer ACQ
performs three steps. First, all non-empty subsets of S, S1, S2, · · · ,
S2l−1 (l=|S|), are enumerated. Then, for each subset Si(1≤i ≤
2l-1), we verify the existence of Gk[Si] and compute it when it
exists (We postpone to discuss the details). Finally, we output the
subgraphs having the most shared keywords among all Gk[Si].
One major drawback of the straightforward method is that we
need to compute 2l −1 subgraphs (i.e., Gk[Si]). For large values
of l, the computation overhead renders the method impractical, and
we do not further consider this method in the paper. To alleviate
this issue, we propose the following two-step framework.
4.1
Two-Step Framework
The two-step framework is mainly based on the following anti-
monotonicity property.
LEMMA 1
(ANTI-MONOTONICITY). Given a graph G, a ver-
tex q ∈G and a set S of keywords, if there exists a subgraph Gk[S],
then there exists a subgraph Gk[S′] for any subset S′ ⊆S.
All the proofs of lemmas studied in this paper can be found in the
full version [29]. The anti-monotonicity property allows us to stop
examining all the super sets of S′(S′ ⊆S), once have veriﬁed that
Gk[S′] does not exist. The basic solution begins with examining
the set, Ψ1, of size-1 candidate keyword sets, i.e., each candidate
contains a single keyword of S. It then repeatedly executes the
following two key steps, to retrieve the size-2 (size-3, . . . ) qualiﬁed
keyword subsets until no qualiﬁed keyword sets are found.
• Veriﬁcation. For each candidate S′ in Ψc (initially c=1), mark
S′ as a qualiﬁed set if Gk[S′] exists.
• Candidate generation. For any two current size-c qualiﬁed key-
word sets which only differ in one keyword, union them as a new
expanded candidate with size-(c+1), and put it into set Ψc+1, if all
its subsets are qualiﬁed, by Lemma 1.
Among the above steps, the key issue is how to compute Gk[S′].
Since Gk[S′] should satisfy the structure cohesiveness (i.e., mini-
mum degree at least k) and keyword cohesiveness (i.e., every ver-
tex contains keyword set S′). Intuitively, we have two approaches
to compute Gk[S′]: either searching the subgraph satisfying de-
gree constraint ﬁrst, followed by further reﬁning with keyword con-
straints (called basic-g); or vise versa (called basic-w). These
two algorithms form our baseline solutions. Their pseudocodes are
presented in the appendix of the full version [29].
5.
CL-TREE INDEX
The major limitation of basic-g and basic-w is that they
need to ﬁnd the k- d
cores and do keyword ﬁltering repeatedly. This
makes the community search very inefﬁcient. To achieve higher
query efﬁciency, we propose a novel index, called CL-tree (Core
Label tree), which organizes both the k- d
cores and keywords into a
tree structure. Based on the index, the efﬁciency of answering ACQ
and its variants can be improved signiﬁcantly. We ﬁrst introduce
the index in Section 5.1, and then propose two index construction
methods in Section 5.2.
5.1
Index Overview
The CL-tree index is built based on the key observation that cores
are nested. Speciﬁcally, a (k+1)- d
core must be contained in a k-
d
core. The rationale behind is, a subgraph has a minimum degree at
least k+1 implies that it has a minimum degree at least k. Thus, all
k- d
cores can be organized into a tree structure3. We illustrate this in
Example 2.
3We use “node” to mean “CL-tree node” in this paper.
4



## Page 5

0
1
1
2
3
ABCD
ABCDE
ABCDEFG
ABCDE
FGHIJ
HI
(a) tree structure
w: A
x: A,B,C,D
y: A,C,D
z: D
y: E
z: E
x: G
y: F, G 
x: I
y: H
z: H
0
1
1
2
3
ABCD
E
FG
J
HI
r1
r2
r3
x: J
(b) CL-tree index
Figure 4: An example CL-tree index.
EXAMPLE 2. Consider the graph in Figure 3(a). All the k-
d
cores can be organized into a tree as shown in Figure 4(a). The
height of the tree is 4. For each tree node, we attach the core num-
ber and vertex set of its corresponding k- d
core.
From the tree structure in Figure 4(a), we conclude that, if a
(k+1)- d
core (denoted as Ck+1) is contained in a k- d
core (denoted as
Ck), then there is a tree node corresponding to Ck+1 and its parent
node corresponds to Ck. Besides, the height of the tree is at most
kmax + 1, where kmax is the maximum core number.
The tree structure in Figure 4(a) can be stored compactly, as
shown in Figure 4(b). The key observation is that, for any internal
node p in the tree, the vertex sets of its child nodes are the subsets
of p’s vertex set, because of the inclusion relationship. To save s-
pace cost, we can remove the redundant vertices that are shared by
p’s child nodes from p’s vertex set. After such removal, we obtain a
compressed tree, where each graph vertex appears only once. This
structure constitutes the CL-tree index, the nodes of which are fur-
ther augmented by inverted lists (Figure 4(b)). For each keyword e
that appears in a CL-tree node, a list of IDs of vertices whose key-
word sets contain e is stored. For example, in node r3, the inverted
list of keyword y contains {A, C, D}. As discussed later, given a
keyword set T, these inverted lists allow efﬁcient retrieval of ver-
tices whose keyword sets contain T. To summarize, each CL-tree
node contains four elements:
• coreNum: the core number of the k- d
core;
• vertexSet: a set of graph vertices;
• invertedList: a list of < key, value > pairs, where the key is a
keyword contained by vertices in vertexSet and the value is the
list of vertices in vertexSet containing key;
• childList: a list of child nodes.
Figure 4(b) depicts the CL-tree index for the example graph in
Figure 3(a), the elements of each tree node are labeled explicitly.
Using the CL-tree, the following two key operations used by our
query algorithms (Section 6), can be performed efﬁciently.
• Core-locating. Given a vertex q and a core number c, ﬁnd the
k- d
core with core number c containing q, by traversing the CL-tree.
• Keyword-checking. Given a k- d
core, ﬁnd vertices which contain
a given keyword set, by intersecting the inverted lists of keywords
contained in the keyword set.
Remarks. The CL-tree can also support k- d
core queries on gen-
eral graphs without keywords. For example, it can be applied to
ﬁnding k- d
core in previous community search methods [27].
Space cost. Since each graph vertex appears only once and each
keyword only needs constant space cost, the space cost of keeping
such an index is O(bl ·n), where bl denotes the average size of W(v)
over V . Thus, the space cost is linear to the size of G.
5.2
Index Construction
To build the CL-tree index, we propose two methods, basic
and advanced, as presented in Section 5.2.1 and 5.2.2.
5.2.1
The Basic Method
As k- d
cores of a graph are nested naturally, it is straightforward
to build the CL-tree recursively in a top-down manner. Speciﬁcally,
we ﬁrst generate the root node for 0-core, which is exactly the entire
graph. Then, for each k- d
core of 1-core, we generate a child node
for the root node. After that, we only remain vertices with core
numbers being 0 in the root node. Then for each child node, we
can generate its child nodes in the similar way. This procedure is
executed recursively until all the nodes are well built.
Algorithm 1 Index construction: basic
1: function BUILDINDEX(G(V, E))
2:
coreG[ ] ←k-core decomposition on G;
3:
k ←0, root ←(k, V );
4:
BUILDNODE(root, 0);
5:
build an inverted list for each tree node;
6:
return root;
7: function BUILDNODE(root, k)
8:
k ←k + 1;
9:
if k ≤kmax then
10:
obtain Uk from root;
11:
compute the connected components for the induced
graph on Uk;
12:
for each connected component Ci do
13:
build a tree node pi ←(k, Ci.vertexSet);
14:
add pi into root.childList;
15:
remove Ci’s vertex set from root.vertexSet;
16:
BUILDNODE(pi, k);
Algorithm 1 illustrates the pseudocodes. We ﬁrst do k-core de-
composition using the linear algorithm [2], and obtain an array
coreG[ ](line 2), where coreG[i] denotes the core number of ver-
tex i in G. We denote the maximal core number by kmax. Then,
we initialize the root node by the core number k=0 and V (line
3). Next, we call the function BUILDNODE to build its child nodes
(line 4). Finally, we build an inverted list for each tree node and
obtain a well built CL-tree (lines 5-6).
In BUILDNODE, we ﬁrst update k and obtain the vertex set Uk
from root.vertexSet, which is a set of vertices with core numbers
being at least k. Then we ﬁnd all the connected components from
the subgraph induced by Uk (lines 8-11). Since each connected
component Ci corresponds to a k- d
core, we build a tree node pi
with core number k and the vertex set of Ci, and then link it as a
child of root (lines 12-14). We also update root’s vertex set by
removing vertices (line 15), which are shared by Ci. Finally, we
call the BUILDNODE function to build pi’s child nodes recursively
until all the tree nodes are created (line 16).
Complexity analysis. The k-core decomposition can be done
in O(m). The inverted lists of each node can be built in O(bl ·
n). In function BUILDNODE, we need to compute the connected
components with a given vertex set, which costs O(m) in the worst
case. Since the recursive depth is kmax, the total time cost is O(m·
kmax + bl · n). Similarly, the space complexity is O(m + bl · n).
5.2.2
The Advanced Method
While the basic method is easy to implement, it meets efﬁ-
ciency issues when both the given graph size and its kmax value
are large. For instance, when given a clique graph with n vertices
(i.e., edges exist between every pair of nodes), the value of kmax is
n–1. Therefore, the time complexity of the basic method could
be O((m+bl)·n), which may lead to low efﬁciency for large-scale
5



## Page 6

graphs. To enable more efﬁcient index construction, we propose
the advanced method, whose time and space complexities are
almost linear with the size of the input graph.
The advanced method builds the CL-tree level by level in a
bottom-up manner. Speciﬁcally, the tree nodes corresponding to
larger core numbers are created prior to those with smaller core
numbers. For ease of presentation, we divide the discussion into
two main steps: creating tree nodes and creating tree edges.
1. Creating tree nodes. We observe that, if we acquire the
vertices with core numbers at least c and denote the induced sub-
graph on the vertices as Tc, then the connected components of Tc
have one-to-one correspondence to the c- d
cores. A simple algorith-
m would be, searching connected components for Tc(0 ≤c ≤
kmax) independently, followed by creating one node for each dis-
tinct component. This algorithm apparently costs O(kmax · m)
time, as computing connected components takes linear time.
However, we can do better if we can incrementally update the
connected components in a level by level manner (i.e., maintain the
connected components of Tc+1 from those of Tc). We note that,
such a node creation process is feasible by exploiting the classi-
cal union-ﬁnd forest [1]. Generally speaking, the union-ﬁnd forest
enables efﬁcient maintenance of connected components of a graph
when edges are incrementally added. Using union-ﬁnd forest to
maintain connected components follows a process of edge exam-
ination. Initially, each vertex is regarded as a connected compo-
nent. Then, edges are examined one by one. During the examine
process, two components are merged together when encounters an
edge connecting them. To achieve an efﬁcient merge of compo-
nents, the vertices in the component form a tree. The tree root acts
as the representative vertex of the component. As such, merging
two components is essentially linking two root vertices together.
To guarantee the CL-tree nodes are formed in a bottom-up manner,
we assign an examine priority to each edge. The priority is deﬁned
by the larger value of the two core numbers corresponding to the
two end vertices of an edge. The edges associated to vertices with
larger core numbers are examined ﬁrst.
2. Creating tree edges. Tree edges are also inserted during the
graph edge examination process. In particular, when we examine
a vertex v with a set, B, of its neighbors, whose core numbers are
larger than coreG[v], we require that the tree node containing v
should link to the tree node containing the vertex, whose core num-
ber is the smallest among all the vertices in B. Nevertheless, the
classical union-ﬁnd forest is not able to maintain such information.
To address this issue, we thus propose an auxiliary data structure,
called Anchored Union-Find (details of AUF are in [29]), based
on the classical union-ﬁnd forest. We ﬁrst deﬁne anchor vertex.
DEFINITION 3
(ANCHOR VERTEX). Given a connected sub-
graph G′ ⊆G, the anchor vertex is the vertex with core number
being min{coreG[v]|v ∈G′}.
The AUF is an extension of union-ﬁnd forest, in which each tree
has an anchor vertex, and it is attached to the root node. In CL-
tree, for any node p with corresponding k- d
core Ck, its child nodes
correspond to the k- d
cores, which are contained by Ck and have core
numbers being the most close to the core number of node p. This
implies that, when building the CL-tree in a bottom-up manner, we
can maintain the anchor vertices for the k- d
cores dynamically, and
they can be used to link nodes with their child nodes. In addition,
we maintain a vertex-node map, where the key is a vertex and the
value is the tree node contains this vertex, for locating tree nodes.
The pseudocodes and analysis are reported in the full version [29].
Complexity analysis. With our proposed AUF, we can reduce
the complexity of CL-tree construction to O(m · α(n)), where
C
D
A
F
E
G
B
H
N
H
M
EFG
ABCD
0
1
1
2
3
IJKL
J
K
L
I
M
B(B)
C
A
D
k=3
K(K)
J
I
L
B(E)
C
A
D
F
E
G
k=2
k=1
K(K)
J
I
L
B(H)
C
A
D
F
E
G H
K(M)
J
I
L M
3
A B C D E F G H
N
I
J K L M N
Vertex-node map:
Anchored union-find forests:
Sets
Vextex IDs
V0
N
V1
H, M
V2
E, F, G
V3
A, B, C, D, I, J, K, L
p1
p2
p3
p4
p5
p6
Figure 5: An index built by advanced method.
α(n), the inverse Ackermann function, is less than 5 for all re-
motely practical values of n [1].
EXAMPLE 3. Figure 5 depicts an example graph with 14 ver-
tices A, · · · , N. Vi denotes the set of vertices whose core number-
s are i. When k=3, we ﬁrst generate two leaf nodes p1 and p2,
then update the AUF, where roots’ anchor vertices are in the round
brackets. When k=2, we ﬁrst generate node p3, then link it to p1,
and then update the AUF forest. When k=1, we ﬁrst generate nodes
p4 and p5. Speciﬁcally, to ﬁnd the child nodes of p4, we ﬁrst ﬁnd
its neighbor A, then ﬁnd A’s parent B using current AUF forest.
Since the anchor vertex of B is E and E points to p3 in the inverted
array, we add p3 into p4’s child List. When k=0, we generate p6
and ﬁnish the index construction.
Index maintenance. We now brieﬂy discuss an incremental ver-
sion of the CL-tree construction algorithm, which can handle the
changes of keywords and graph edges, without rebuilding the CL-
tree from scratch. To insert (or remove) a keyword of a vertex, we
just need to update the invertedList of the CL-tree node contain-
ing the vertex. To insert (or remove) a graph edge, we borrow the
results from [20], which discusses how to maintain a k-core. A
more detailed discussion can be found in our report [29]. We plan
to investigate this issue more extensively in the future.
6.
QUERY ALGORITHMS
In this section, we present three query algorithms based on the
CL-tree index. Based on how we verify the candidate keyword sets,
we divide our algorithms into incremental algorithms (from exam-
ining smaller candidate sets to larger ones) and decremental algo-
rithm (from examining larger candidate sets to smaller ones). We
propose two incremental algorithms called Inc-S (Incremental
Space efﬁcient) and Inc-T (Incremental Time efﬁcient), to trade
off between the memory consumption and the computational over-
head. We also design a decremental algorithm called Dec (Decremental).
Our interesting ﬁnding is that, while Dec seems not intuitive, it
ranks as the most efﬁcient one. Inc-S and Inc-T are presented
in Section 6.1. Dec is introduced in Section 6.2.
6.1
The Incremental Algorithms
While the high-level idea of incremental algorithms resembles
the basic solutions (see Section 4), Inc-S and Inc-T advance
them with the exploitation of the CL-tree. Speciﬁcally, they can al-
ways verify the existence of Gk[S′] within a subgraph of G instead
of the entire graph G. More interestingly, the subgraph for such
veriﬁcations shrinks when the candidate set S′ expands. Therefore,
a large sum of redundant computation is cut off during the veriﬁca-
tion. We present Inc-S and Inc-T in Sections 6.1.1 and 6.1.2.
6



## Page 7

6.1.1
Inc-S Algorithm
We ﬁrst introduce a new concept, called subgraph core num-
ber, which is geared to the main idea of Inc-S.
DEFINITION 4
(SUBGRAPH CORE NUMBER). Given a subgraph
G′ of G, its core number, coreG[G′], is deﬁned as min{coreG[v]|
v ∈G′}.
Inc-S follows the two-step framework (veriﬁcation and can-
didate generation) introduced in Section 4. With the CL-tree, we
improve the veriﬁcation step as follows.
• Core-based veriﬁcation. For each newly generated size-
(c+1) candidate keyword set S′ expanded from size-c sets S1
and S2, mark S′ as a qualiﬁed set if Gk[S′] exists in a sub-
graph of core number max{coreG[Gk[S1]], coreG[Gk[S2]]}.
The core-based veriﬁcation guarantees that, with the expansion
of the candidate keyword sets, the veriﬁcation becomes faster as
it only needs to examine the existence of Gk[S′] in a smaller k-
d
core (Recall that cores with large core numbers are nested in the
cores with small core numbers). The correctness of such shrunk
veriﬁcation range is guaranteed by the following lemma.
LEMMA 2. Given two subgraphs Gk[S1] and Gk[S2] of a graph
G, for a new keyword set S′ generated from S1 and S2 (i.e., S′ =
S1 ∪S2), if Gk[S′] exists, then it must appear in a k- d
core with core
number at least
max{coreG[Gk[S1]], coreG[Gk[S2]]}.
(1)
The veriﬁcation process can be further accelerated by checking
the numbers of vertices and edges, as indicated by Lemma 3.
LEMMA 3. Given a connected graph G(V, E) with n=|V | and
m=|E|, if m −n < k2−k
2
−1, there is no k- d
core in G.
This lemma implies that, for a connected subgraph G′, whose
edge and vertex numbers are m and n, if m −n < k2−k
2
−1, then
we cannot ﬁnd Gk[S′] from G′.
We present Inc-S in Algorithm 2. The input is a CL-tree rooted
at root, a query vertex q, a positive integer k and a keyword set S.
We apply core-locating on the CL-tree to locate the internal
nodes whose corresponding k- d
cores contain q (line 2). Note that
their core numbers are in the range of [k, coreG[q]], as required by
the structure cohesiveness. Then, we set l=0, indicating the sizes
of current keyword sets, and initialize a set Ψ of < S′, c > pairs,
where S′ is a set containing a keyword from S and c is the initial
core number k (line 3). Note that we skip those keywords, which
are in S, but not in W(q). In the while loop (lines 4-18), for each
< S′, c > pair, we ﬁrst perform keyword-checking to ﬁnd
G[S′] using the keyword inverted lists of the subtree rooted at node
rc. If we cannot ensure that G[S′] does not contain a k- d
core by
Lemma 3, we then ﬁnd Gk[S′] from G[S′] (lines 8-9). If Gk[S′]
exists, we put S′ with its core number into the set Φl (lines 10-11).
Next, if Φl is nonempty, we generate new candidates by calling
GENECAND(Φl), which is detailed in the full version [29]. For
each candidate S′ in Ψ, we compute the core number using Lem-
ma 2 and update it as a pair in Ψ (lines 12-17); otherwise, we stop
(line 18). Finally, we output the communities of the latest veriﬁed
keyword sets (line 19).
EXAMPLE 4. Consider the graph in Figure 3(a) and its index
in Figure 4(b). Let q=A, k=1 and S={w, x, y}. By Algorithm 2,
we ﬁrst ﬁnd 3 root nodes r1, r2 and r3. In the ﬁrst while loop, we
ﬁnd 2 qualiﬁed keyword sets {x}and{y} with core numbers being
3 and 1. By Lemma 2, we only need to verify the new candidate
keyword set {x, y} under node r3.
Algorithm 2 Query algorithm: Inc-S
1: function QUERY(G, root, q, k, S)
2:
ﬁnd subtree root nodes rk, rk+1, · · · , rcoreG[q];
3:
initialize l=0, Ψ using S;
4:
while true do
5:
l ←l + 1; Φl ←∅;
6:
for each < S′, c > ∈Ψ do
7:
ﬁnd G[S′] under the root rc;
8:
if G[S′] is not pruned by Lemma 3 then
9:
ﬁnd Gk[S′] from G[S′];
10:
if Gk[S′] exists then
11:
Φl.add(< S′, coreG[Gk[S′]] >);
12:
if Φl ̸= ∅then
13:
Ψ ←GENECAND(Φl);
14:
for each S′ in Ψ do
15:
if S′ is generated from S1 and S2 then
16:
c ←max{coreG[Gk[S1]], coreG[Gk[S2]]};
17:
Ψ.update(S′, < S′, c >);
18:
else break;
19:
output the communities of keyword sets in Φl−1;
6.1.2
Inc-T Algorithm
We begin with a lemma which inspires the design of Inc-T.
LEMMA 4. Given two keyword sets S1 and S2, if Gk[S1] and
Gk[S2] exist, we have
Gk[S1 ∪S2] ⊆Gk[S1] ∩Gk[S2].
(2)
This lemma implies, if S′ is generated from S1 and S2, we can
ﬁnd Gk[S′] from Gk[S1] ∩Gk[S2] directly. Since every vertex
in Gk[S1] ∩Gk[S2] contains both S1 and S2, we do not need to
consider the keyword constraint again when ﬁnding Gk[S′].
Based on Lemma 4, we introduce a new algorithm Inc-T. Dif-
ferent from Inc-S, Inc-T maintains Gk[S′] rather than coreG[
Gk[S′]] for each qualiﬁed keyword set S′. As we will demonstrate
later, Inc-T is more effective for shrinking the subgraphs con-
taining the ACs, and thus more efﬁcient. As a trade-off for better
efﬁciency, Inc-T consumes more memory as it needs to store a
list of subgraph Gk[S′] in memory.
Algorithm 3 presents Inc-T. We ﬁrst apply core-locating
to ﬁnd the k- d
core containing q from the CL-tree (line 2). Then, we
set l=0, indicating the sizes of current keyword sets, and initialize
a set Ψ of < S′, bG > pairs, where S′ is a set containing a keyword
from S and bG is the k- d
core. The while loop (lines 4-18) is simi-
lar with that of Inc-S. The main differences are that: (1) for each
qualiﬁed keyword set S′, Inc-T keeps Gk[S′] in memory (line
11); and (2) for each candidate keyword set S′ generated from S1
and S2, Inc-T ﬁnds Gk[S′] from Gk[S1] ∩Gk[S2] directly with-
out further keyword veriﬁcation (lines 6-9, 16).
EXAMPLE 5. Continue the graph and query (q=A, k=1, S={w,
x, y}) in Example 4. By Inc-T, we ﬁrst ﬁnd G1[{x}] and G1[{y}],
whose vertex sets are {A, B, C, D} and {A, C, D, E, F, G}. Then
to ﬁnd G1[{x, y}], we only need to search it from the subgraph, in-
duced by the vertex set {A, C, D}.
6.2
The Decremental Algorithm
The decremental algorithm, denoted by Dec, differs from previ-
ous query algorithms not only on the generation of candidate key-
word sets, but also on the veriﬁcation of candidate keyword sets.
1. Generation of candidate keyword sets. Dec exploits the
key observation that, if S′ (S′ ⊆S) is a qualiﬁed keyword set,
then there are at least k of q’s neighbors containing set S′. This
7



## Page 8

Algorithm 3 Query algorithm: Inc-T
1: function QUERY(G, root, q, k, S)
2:
ﬁnd the k- d
core, which contains q;
3:
initialize l=0, Ψ using S;
4:
while true do
5:
l ←l + 1; Φl ←∅;
6:
for each < S′, bG > ∈Ψ do
7:
ﬁnd G[S′] from bG;
8:
if G[S′] is not pruned by Lemma 3 then
9:
ﬁnd Gk[S′] from G[S′];
10:
if Gk[S′] exists then
11:
Φl.add(< S′, Gk[S′] >);
12:
if Φl ̸= ∅then
13:
Ψ ←GENECAND(Φl);
14:
for each S′ ∈Ψ do
15:
if S′ is generated from S1 and S2 then
16:
bG ←Gk[S1] ∩Gk[S2];
17:
Ψl.update(S′,< S′, bG >);
18:
else break;
19:
output the communities of keyword sets in Φl−1;
is because every vertex in Gk[S′] must has degree at least k. This
observation implies, we can generate all the candidate keyword set-
s directly by using the query vertex q and q’s neighbors, without
touching other vertices.
Speciﬁcally, we consider q and q’s neighbor vertices. For each
vertex v, we only select the keywords, which are contained by S
and at least k of its neighbors. Then we use these selected key-
words to form an itemset, in which each item is a keyword. After
this step, we obtain a list of itemsets. Then we apply the well s-
tudied frequent pattern mining algorithms (e.g., Apriori [13] and
FP-Growth [14]) to ﬁnd the frequent keyword combinations, each
of which is a candidate keyword set. Since our goal is to gener-
ate keyword combinations shared by at least k neighbors, we set
the minimum support as k. In this paper, we use the well-known
FP-Growth algorithm [14].
Q:{v,x,y,z}
A:{v,x,y,z}
B:{v,x}
D:{x,y,z}
E:{w,x,y,z}
C:{v,y}
F:{v, w}
(a) a query vertex
k=3
Set
Keyword sets
Ψ1
{v},{x},{y},{z}
Ψ2
{x,y},{x,z},{y,z}
Ψ3
{x,y,z}
(b) candidates
Figure 6: An example of candidate generation.
EXAMPLE 6. Consider a query vertex Q (k=3, S={v, x, y, z})
with 6 neighbors in Figure 6(a), where the selected keywords of
each vertex are listed in the curly braces. By FP-Growth, 8 can-
didate keyword sets) are generated, as shown in Figure 6(b). Ψi
denotes the set of keyword sets with sizes being i.
2. Veriﬁcation of candidate keyword sets. As candidates can
be obtained using S and q’s neighbors directly, we can verify them
either incrementally as that in Inc-S, or in a decremental manner
(larger candidate keyword sets ﬁrst and smaller candidate keyword
sets later). In this paper, we choose the latter manner. The rationale
behind is that, for any two keyword sets S1 ⊆S2, the number
of vertices containing S2 is usually smaller than that of S1, which
implies S2 can be veriﬁed more efﬁciently than S1.
Based on the above discussions, we design Dec as shown in Al-
gorithm 4. We ﬁrst generate candidate keyword sets using S and
Algorithm 4 Query algorithm: Dec
1: function QUERY(G, root, q, k, S)
2:
generate Ψ1, Ψ2, · · · , Ψh using S and q’s neighbors;
3:
ﬁnd the subtree root node rk;
4:
create R1, R2, · · · , Rh′ by using subtree rooted at rk;
5:
l ←h; Q ←∅;
6:
bR ←Rh ∪· · · ∪Rh′;
7:
while l ≥1 do
8:
for each S′ ∈Ψl do
9:
ﬁnd G[S′] from the subgraph induced on bR;
10:
ﬁnd Gk[S′] from G[S′];
11:
if Gk[S′] exists then Q.add(Gk[S′]);
12:
if Q=∅then
13:
l ←l −1;
14:
bR ←bR ∪Rl;
15:
else break;
16:
output communities in Q;
q’s neighbors by FP-Growth algorithm (line 2). Then, we apply
core-locating to ﬁnd the root (with core number k) of the sub-
tree from CL-tree, whose corresponding k- d
core contains q (line 3).
Next, we traverse the subtree rooted at rk and ﬁnd vertices which
share keywords with q (line 4). Ri denote the sets of vertices shar-
ing i keywords with q. Then, we initialize l as h (line 5), as we
verify keyword sets with the largest size h ﬁrst. We maintain a set
bR dynamically, which contains vertices sharing at least l keywords
with q (line 6). In the while loop, we examine candidate keyword
sets in the decremental manner. For each candidate S′ ∈Ψl, we
ﬁrst try to ﬁnd G[S′], then ﬁnd Gk[S′], and put Gk[S′] into Q if it
exists (lines 8-11). Finally, if we have found at least one qualiﬁed
community, we stop at the end of this loop and output Q; otherwise,
we examine smaller candidate keyword sets in next loop.
7.
EXPERIMENTS
We now present the experimental results. Section 7.1 discusses
the setup. We discuss the results in Sections 7.2 and 7.3.
7.1
Setup
We consider four real datasets. For Flickr 4, a vertex represents
a user, and an edge denotes a “follow” relationship between two
users. For each vertex, we use the 30 most frequent tags of its as-
sociated photos as its keywords. For DBLP 5, a vertex denotes an
author, and an edge is a co-authorship relationship between two au-
thors. For each author, we use the 20 most frequent keywords from
the titles of her publications as her keywords. In the Tencent graph
provided by the KDD contest 2012 6, a vertex is a person, an orga-
nization, or a microblog group. Each edge denotes the friendship
between two users. The keyword set of each vertex is extracted
from a user’s proﬁle. For the DBpedia 7, each vertex is an entity,
and each edge is the relationship between two entities. The key-
words of each entity are extracted by the Stanford Analyzer and
Lemmatizer. Table 3 shows the number of vertices and edges, the
kmax value, a vertex’s average degree bd, and its keyword set size bl.
To evaluate ACQs, we set the default value of k to 6. The input
keyword set S is set to the whole set of keywords contained by the
query vertex. For each dataset, we randomly select 300 query ver-
tices with core numbers of 6 or more, which ensures that there is a
4https://www.flickr.com/
5http://dblp.uni-trier.de/xml/
6http://www.kddcup2012.org/c/
kddcup2012-track1
7http://dbpedia.org/datasets
8



## Page 9

Table 3: Datasets used in our experiments.
Dataset
Vertices
Edges
kmax
bd
bl
Flickr
581,099
9,944,548
152
17.11
9.90
DBLP
977,288
3,432,273
118
7.02
11.8
Tencent
2,320,895
50,133,369
405
43.2
6.96
DBpedia
8,099,955
71,527,515
95
17.66
15.03
k-core containing each query vertex. Each data point is the average
result for these 300 queries. We implement all the algorithms in
Java, and run experiments on a machine having a quad-core Intel
i7-3770 processor, and 32GB of memory, with Ubuntu installed.
7.2
Results on Effectiveness
We now study the effectiveness of ACQ, and compare it with
existing CD and CS methods. We then discuss a case study.
7.2.1
ACQ Effectiveness
We ﬁrst deﬁne two measures, namely CMF and CPJ, for evaluat-
ing the keyword cohesiveness of the communities. Let C(q)={C1, C2,
· · · , CL} be the set of L communities returned by an algorithm for
a query vertex q ∈V (Note that S=W(q)).
• Community member frequency (CMF): this is inspired by
the classical document frequency measure. Consider a keyword x
of q’s keyword set W(q). If x appears in most of the vertices (or
members) of a community Ci, then we regard Ci to be highly cohe-
sive. The CMF uses the occurrence frequencies of q’s keywords in
Ci to determine the degree of cohesiveness. Let fi,h be the number
of vertices of Ci whose keyword sets contain the h-th keyword of
W(q). Then,
fi,h
|Ci| is the relative occurrence frequency of this key-
word in Ci. The CMF is the average of this value over all keywords
in W(q), and all communities in C(q):
CMF(C(q)) =
1
L · |W(q)|
L
X
i=1
|W (q)|
X
h=1
fi,h
|Ci|
(3)
Notice that CMF(C(q)) ranges from 0 to 1. The higher its value,
the more cohesive is a community.
• Community pair-wise Jaccard (CPJ): this is based on the
similarity between the keyword sets of any pair of vertices of com-
munity Ci. We adopt the Jaccard similarity, which is commonly
used in the IR literature. Let Ci,j be the j-th vertex of Ci. The CPJ
is then the average similarity over all pairs of vertices of Ci, and all
communities of C(q):
CPJ(C(q)) = 1
L
L
X
i=1


1
|Ci|2
|Ci|
X
j=1
|Ci|
X
k=1
W(Ci,j) ∩W(Ci,k)

W(Ci,j) ∪W(Ci,k)


(4)
The CPJ(C(q)) value has a range of 0 and 1. A higher value of
CPJ(C(q)) implies better cohesiveness.
1. Effect of common keywords. We examine the impact of
the AC-label length (i.e., the number of keywords shared by all
the vertices of the AC) on keyword cohesiveness. We collect ACs
containing one to ﬁve keywords, and then group the ACs according
to their AC-label lengths. The average CMF and CPJ value of each
group is shown in Figure 7. For all the datasets, when the AC-label
lengths increase, both CMJ and CPJ value rises. This justiﬁes the
use of the maximal AC-label length as the criterion of returning an
AC in our ACQ Problem.
2. Comparison with existing CD methods As mentioned a-
head, the existing CD methods for attributed graph can be adapt-
ed for community search. We choose to adapt CODICIL [24] for
comparison. The main reasons are: (1) it has been tested on the
1
2
3
4
5
0
0.2
0.4
0.6
0.8
1
the nubmer of shared keywords
CMF
 
 
Flickr
DBLP
 
 
Tencent
DBpedia
(a) CMF
1
2
3
4
5
0
0.2
0.4
0.6
0.8
1
the nubmer of shared keywords
CPJ
 
 
Flickr
DBLP
 
 
Tencent
DBpedia
(b) CPJ
Figure 7: AC-label length.
(a) Keyword (CMF)
(b) Keyword (CPJ)
(c) Structure (Avg. degree)
(d) Structure (degree ≥6)
Figure 8: Comparing with community detection method.
ever reported largest attributed graph (vertex number:3.6M); (2) it
identiﬁes communities of comparable or superior quality than those
of many existing methods like [22, 31]; and (3) it runs faster than
many existing methods. Since CODICIL needs users to specify the
number of clusters expected, we set the numbers as 1K, 5K, 10K,
50K and 100K. The corresponding adapted algorithms are named
as Cod1K, · · · , Cod100K respectively. Other parameter settings
are the same as those in [24]. We ﬁrst run these algorithms ofﬂine
to obtain all the communities. Given a query vertex q, they return
communities containing q as the results.
We consider both keyword and structure for evaluating commu-
nity quality. (1) Keyword: Figures 8(a) and (b) show that ACQ
(implemented by Dec) always performs the best, in terms of CMF
and CPJ. (2) Structure: As CODICIL has no guarantee on vertices’
minimum degrees, it is unfair to compare them using this metric.
We intuitively compare their structure cohesiveness by reporting
the average degree of the vertices in the communities and the per-
centage of vertices having degrees of 6 or more. When the number
of clusters in CODICIL is too large or too small, the structure co-
hesiveness becomes weak, as shown in Figures 8(c) and (d). ACQ
always performs better than CODICIL, even when its number of
cluster is well set (e.g., Cod10K and Cod50K on DBLP dataset).
3. Comparison with existing CS methods. The existing meth-
ods mainly focus on non-attributed graphs.
We implement two
state-of-the-art methods: Global [27] and Local [5]. Both of
them use the metric minimum degree, we thus focus on the key-
word cohesiveness. Figure 9 shows the CMF and CPJ values for
the four datasets. We can see that the keyword cohesiveness of
ACQ is superior to both Global and Local, because ACQ con-
siders vertex keywords, while Global and Local do not.
7.2.2
A Case Study
We next perform a case study on the DBLP dataset, in which we
consider two renowned researchers in database and data mining:
Jim Gray and Jiawei Han. We use k = 4 here. We use Cod50K to
9



## Page 10

(a) CMF
(b) CPJ
Figure 9: Comparing with community search methods.
represent CODICIL for further analysis. We mainly consider the
input query keyword set S, keywords and sizes of communities.
1. Effect of S. Figure 10 shows two ACs of Jiawei (The AC-
labels are shown in the captions), where the set S are set as {analysis,
mine, data, information, network} and {mine, data, pattern, database}
respectively. These two groups of Jiawei’s collaborators are in-
volved in graph analysis (Figure 10(a)) and pattern mining (Fig-
ure 10(b)). Although these researchers all have close co-author re-
lationship with Jiawei, the use of the input keyword set S enables
the identiﬁcation of communities with different research themes.
For Jim, we can obtain similar results as discussed in Section 1
(Figure 2). While for CODICIL, it is not clear how to consider the
input keyword set S, and we thus do not show the results.
Jiawei Han
Xifeng Yan
Philip S. Yu
Yizhou Sun
Tianyi Wu
(a) {analysis, data, infor-
mation, network}
Jiawei Han
Jeffrey Xu Yu
Philip S. Yu
Jianyong Wang
Jian Pei
Guozhu Dong
(b) {mine,
data,
pattern,
database}
Figure 10: Jiawei Han’s ACs.
10
20
30
0
0.2
0.4
0.6
0.8
1
MF
 
 
Cod50K
Global
Local
ACQ
(a) Jim Gray
10
20
30
0
0.2
0.4
0.6
0.8
1
MF
 
 
Cod50K
Global
Local
ACQ
(b) Jiawei Han
Figure 11: Frequency distribution of keywords.
2. Keyword analysis. We analyze the frequency distribution of
keywords in their communities. Speciﬁcally, given a keyword wh,
we deﬁne the member frequency (MF) of wh as: MF(wh, C(q)) =
1
L
L
P
i=1
fi,h
|Ci|.
The MF measures the occurrence of a keyword in
C(q). For each Cq generated by an algorithm, we select 30 key-
words with the highest MF values. We report the MF of each key-
word in descending order of their MF values in Figure 11. We see
that ACQ has the highest MF values for the top 20 keywords. Thus,
the keywords associated with the communities generated by ACQ
tend to repeat among the community members.
The number of distinct keywords of ACQ communities is also
the fewest, as shown in Table 4. For example, the k- d
core returned
by Global has over 139K distinct keywords, about 2,300 times
more than that returned by ACQ (less than 60 keywords). While the
semantics of the k- d
core can be difﬁcult to understand, the small
Table 4: # distinct keywords of communities.
Researcher
Cod50K
Global
Local
ACQ
Jim Gray
134
139,881
60
44
Jiawei Han
140
139,881
58
54
number of distinct keywords of AC makes it easier to understand
why the community is so formed. We further report the keywords
with the 6 highest MF values in the communities in Tables 5 and
6. We can see that, the top-6 keywords are highly related to their
input query keyword sets. Note that the top-6 keywords of Global
are the same for both Jim and Jiawei, as they are in the same k-
d
core. Thus, they cannot be used to characterize the communities
speciﬁcally related to Jim and Jiawei. The overall results show that,
ACQ performs better than other methods.
3. Effect of k on community size. We vary the value of k and re-
port the average size of communities in Figure 12. We can see that
the communities returned by Global are extremely large (more
than 105), which can make them difﬁcult for a query user to ana-
lyze. The community size of Local increases sharply when k=8.
In this situation, Local returns the same community as Global.
The size of an AC is relatively insensitive to the change of k, as AC
contains around a hundred vertices for a wide range of values of k.
4. GPM Results. We have examined communities produced by
Graph Pattern Matching (GPM) algorithms on the DBLP dataset.
We consider a “Star-a” pattern, which contains a vertices linked
to the query vertex q. A keyword set S is randomly drawn from Jim
Gray’s keyword sets, i.e., W(q). Each vertex of the pattern is asso-
ciated with S. We vary the size of S; for each |S|, we obtain 100
different sets. We then execute the Match algorithm [9] with its
default settings. Table 7 shows the fraction of GPM queries return-
ing non-empty communities. When |S| ≥3, only a small fraction
of Star-a patterns yields non-empty subgraphs. These subgraphs
vary, depending on the topology and keyword sets associated with
the patterns. Hence, if GPM is used to ﬁnd communities, the user
has to be careful in choosing the right pattern.
Table 5: Top-6 keywords (Jim Gray).
Algo.
Keywords
Cod50K
server, archive, sloan, digital, database
Global
use, system, model, network, analysis, data
Local
database, system, multipetabyte, data, lsst, story
ACQ
sloan, digital, sky, data, sdss, server
Table 6: Top-6 keywords (Jiawei Han).
Algo.
Keywords
Cod50K
information, mine, data, cube, text, network
Global
use, system, model, network, analysis, data
Local
scalable, topical, text, phrase, corpus, mine
ACQ
mine, analysis, data, information, network, heterogen
7.3
Results on Efﬁciency
For each dataset, we randomly select 20%, 40%, 60% and 80%
of its vertices, and obtain four subgraphs induced by these vertex
sets. For each vertex, we randomly select 20%, 40%, 60% and 80%
of its keywords, and obtain four keyword sets.
1. Index construction. Figures 13(a)-13(d) compare the ef-
ﬁciency of Basic and Advanced. We study their main parts,
which build the tree without considering keywords. We denote
them by Basic- and Advanced-. Notice that Advanced per-
forms consistently faster, and scales better, than Basic. When the
subgraph size increases, the performance gap between Advanced
and Basic is enlarged. Similar results can be observed between
Advanced- and Basic-. In addition, we also run the CD method
CODICIL, which takes 32 min, 2 min, 1 day, and 3+ days (we stop
10



## Page 11

20%
40%
60%
80% 100%
0
2000
4000
6000
8000
10000
12000
percentage of vertices
time (ms)
 
 
Basic
Basic−
Advanced
Advanced−
20%
40%
60%
80%
100%
0
0.5
1
1.5
2
2.5
3 x 10
4
percentage of vertices
time (ms)
 
 
Basic
Basic−
Advanced
Advanced−
20%
40%
60%
80%
100%
0
1
2
3
4
x 10
5
percentage of vertices
time (ms)
 
 
Basic
Basic−
Advanced
Advanced−
20%
40%
60%
80%
100%
0
5
10
15
x 10
4
percentage of vertices
time (ms)
 
 
Basic
Basic−
Advanced
Advanced−
(a) Flickr (index scalability)
(b) DBLP (index scalability)
(c) Tencent (index scalability)
(d) DBpedia (index scalability)
Figure 13: Efﬁciency results of index construction.
4
5
6
7
8
0
200
400
600
800
1000
k
time (ms)
 
 
Global
Local
Dec
4
5
6
7
8
0
200
400
600
k
time (ms)
 
 
Global
Local
Dec
4
5
6
7
8
0
2000
4000
6000
8000
k
time (ms)
 
 
Global
Local
Dec
4
5
6
7
8
0
5000
10000
15000
k
time (ms)
 
 
Global
Local
Dec
(a) Flickr (efﬁciency)
(b) DBLP (efﬁciency)
(c) Tencent (efﬁciency)
(d) DBpedia (efﬁciency)
4
5
6
7
8
10
2
10
3
10
4
k
time (ms)
 
 
basic−g
basic−w
 
 
Inc−S
Inc−T
Dec
4
5
6
7
8
10
2
10
4
10
6
k
time (ms)
 
 
basic−g
basic−w
 
 
Inc−S
Inc−T
Dec
4
5
6
7
8
10
2
10
4
k
time (ms)
 
 
basic−g
basic−w
 
 
Inc−S
Inc−T
Dec
4
5
6
7
8
10
2
10
4
10
6
k
time (ms)
 
 
basic−g
basic−w
 
 
Inc−S
Inc−T
Dec
(e) Flickr (effect of k)
(f) DBLP (effect of k)
(g) Tencent (effect of k)
(h) DBpedia (effect of k)
20%
40%
60%
80%
100%
0
50
100
150
200
percentage of keywords
time (ms)
 
 
Inc−S
Inc−T
Dec
20%
40%
60%
80% 100%
0
500
1000
1500
percentage of keywords
time (ms)
 
 
Inc−S
Inc−T
Dec
20%
40%
60%
80% 100%
0
200
400
600
800
1000
1200
percentage of keywords
time (ms)
 
 
Inc−S
Inc−T
Dec
20%
40%
60%
80% 100%
0
200
400
600
800
1000
percentage of keywords
time (ms)
 
 
Inc−S
Inc−T
Dec
(i) Flickr (keyword scalability)
(j) DBLP (keyword scalability)
(k) Tencent (keyword scalability)
(l) DBpedia (keyword scalability)
20%
40%
60%
80%
100%
0
50
100
150
200
percentage of vertices
time (ms)
 
 
Inc−S
Inc−T
Dec
20%
40%
60%
80% 100%
0
500
1000
1500
percentage of vertices
time (ms)
 
 
Inc−S
Inc−T
Dec
20%
40%
60%
80% 100%
0
200
400
600
800
1000
1200
percentage of vertices
time (ms)
 
 
Inc−S
Inc−T
Dec
20%
40%
60%
80% 100%
0
200
400
600
800
1000
percentage of vertices
time (ms)
 
 
Inc−S
Inc−T
Dec
(m) Flickr (vertex scalability)
(n) DBLP (vertex scalability)
(o) Tencent (vertex scalability)
(p) DBpedia (vertex scalability)
1
3
5
7
9
10
2
10
3
10
4
the number of keywords in S
time (ms)
 
 
basic−g
basic−w
Dec
1
3
5
7
9
10
1
10
2
10
3
10
4
10
5
the number of keywords in S
time (ms)
 
 
basic−g
basic−w
Dec
1
3
5
7
9
10
2
10
4
the number of keywords in S
time (ms)
 
 
basic−g
basic−w
Dec
1
3
5
7
9
10
2
10
4
10
6
the number of keywords in S
time (ms)
 
 
basic−g
basic−w
Dec
(q) Flickr (set S)
(r) DBLP (set S)
(s) Tencent (set S)
(t) DBpedia (set S)
Figure 14: Efﬁciency results of community search.
11



## Page 12

4
5
6
7
8
10
2
10
4
10
6
k
community size
 
 
Global
Local
ACQ
(a) Jim Gray
4
5
6
7
8
10
2
10
4
10
6
k
community size
 
 
Global
Local
ACQ
(b) Jiawei Han
Figure 12: Community size.
Table 7: % GPM queries that return at least one subgraph.
Researcher
|S|
Star-6
Star-8
Star-10
Jim Gray
1
93%
93%
93%
2
68%
60%
56%
3
21%
16%
14%
4
5.0%
3.0%
2.0%
5
0.0%
0.0%
0.0%
it after 3 days) to cluster the vertices of Flickr, DBLP, Tencent and
DBpedia ofﬂine respectively.
2. Efﬁciency of CS methods. Figures 14(a)-14(d) compares our
best algorithm Dec with existing CS methods. We see that Local
performs faster than Global for most cases. Also, Dec, which
uses the CL-tree index, is the fastest.
3. Effect of k. Figures 14(e)-14(h) compare the query efﬁciency
under different k. A lower k renders a larger subgraph, so as the
time costs, for all the algorithms. Note that basic-g performs
faster than basic-w, but are slower than index-based algorithms.
Inc-T performs better than Inc-S, and Dec performs the best.
The performance gaps decrease as k increases.
4. ACQ scalability w.r.t. keyword. Figures 14(i)-14(l) exam-
ines scalability over the fraction of keywords for each vertex. All
the vertices are considered. The running times of the algorithms
increase as more keywords are involved. Dec performs the best.
Next, we present the results about DBpedia, the largest dataset
used in our experiments. Results for other datasets are similar, and
are reported in our report [29] due to space constraints.
5. ACQ scalability w.r.t. vertex. Figures 14(m) and 14(p) re-
ports the scalability over different fraction of vertices. All the key-
words of each vertex are considered. Again, Dec scales the best.
6. Effect of size of S. For each query vertex, we randomly select
1, 3, 5, 7 and 9 keywords to form the query keyword set S. As Dec
performs better than Inc-S and Inc-T, we mainly compare Dec
with the baseline solutions. Figures 14(q)- 14(t) show that the cost
of all algorithms increase with the |S|. Also, Dec is 1 to 3 order-
of-magnitude faster than basic-g and basic-w.
7. Effect of invertedList. We implement Inc-S* and Inc-T*,
which are respective variants of Inc-S and Inc-T, without the in-
vertedList on each CL-tree node. Figure 15 shows the efﬁciency
of Inc-S (Inc-T) and Inc-S* (Inc-T*). We see that Inc-S
(Inc-T) is 1 to 2 order of magnitude faster than Inc-S* (Inc-T*).
The keyword-checking operation, which uses the invertedList, is
frequently performed. The use of invertedList thus improves the
performance of our algorithms signiﬁcantly.
8. Non-attributed graphs. We also test Dec and Local on
non-attributed graphs, by ignoring the keywords of the graph dataset.
The experimental results are shown in Figure 16. For Flickr, Ten-
cent and DBpedia, Dec is consistently faster than Local. In Dec,
cores are organized into the CL-tree structure. Because the height
of the CL-tree is not very high (lower than 405 for all datasets),
the core-locating operation can be done quickly. For DBLP, Dec
is also faster than Local, except when k=4. In DBLP, a paper
often has few (around 3 to 5) co-authors. Since an author may be
closely related to a few co-authors, ﬁnding a 4- d
core in Local can
be done efﬁciently through local expansion. From these experi-
ments, we conclude that Dec can also be efﬁciently executed on
non-attributed graphs.
8.
CONCLUSIONS
An AC is a community that exhibits structure and keyword co-
hesiveness. To facilitate ACQ evaluation, we develop the CL-tree
index and its query algorithms. Our experimental results show that
ACs are easier to interpret than those of existing community detec-
tion/search methods, and they can be “personalized”. Our solutions
are also faster than existing community search algorithms. In the
future, we will study how graph pattern matching techniques can
be used to solve the ACQ problem. We also plan to extend our so-
lutions to support directed and dynamic graphs. We will investigate
algorithms for maintaining the CL-index. We will study the use of
other measures of structure cohesiveness (e.g., k-truss, k-clique)
and keyword cohesiveness (e.g., Jaccard similarity and string edit
distance) in the ACQ deﬁnition.
9.
REFERENCES
[1] https://en.wikipedia.org/wiki/Disjoint-set data structure.
[2] V. Batagelj and M. Zaversnik. An o(m) algorithm for cores
decomposition of networks. arXiv, 2003.
[3] G. Bhalotia et al. Keyword searching and browsing in
databases using banks. In ICDE, 2002.
[4] W. Cui et al. Online search of overlapping communities. In
SIGMOD, 2013.
[5] W. Cui et al. Local search of communities in large graphs. In
SIGMOD, 2014.
[6] B. Ding et al. Finding top-k min-cost connected trees in
databases. In ICDE, 2007.
[7] S. N. Dorogovtsev et al. K-core organization of complex
networks. Physical review letters, 2006.
[8] T. et al. Fast best-effort pattern matching in large attributed
graphs. In KDD, 2007.
[9] W. Fan et al. Graph pattern matching: from intractable to
polynomial time. PVLDB, 2010.
[10] W. Fan et al. Incremental graph pattern matching. In
SIGMOD, 2011.
[11] W. Fan et al. Association rules with graph patterns. PVLDB,
8(12):1502–1513, 2015.
[12] S. Fortunato. Community detection in graphs. Physics
Reports, 486(3):75–174, 2010.
[13] J. Han, M. Kamber, and J. Pei. Data mining: concepts and
techniques. Elsevier, 2011.
[14] J. Han, J. Pei, and Y. Yin. Mining frequent patterns without
candidate generation. In SIGMOD, 2000.
[15] H. He et al. Blinks: ranked keyword searches on graphs. In
SIGMOD, 2007.
[16] X. Huang et al. Querying k-truss community in large and
dynamic graphs. In SIGMOD, 2014.
[17] V. Kacholia et al. Bidirectional expansion for keyword
search on graph databases. In VLDB, 2005.
[18] M. Kargar and A. An. Keyword search in graphs: Finding
r-cliques. PVLDB, 4(10):681–692, 2011.
[19] R.-H. Li, L. Qin, J. X. Yu, and R. Mao. Inﬂuential
community search in large networks. In PVLDB, 2015.
12



## Page 13

4
5
6
7
8
10
3
10
4
k
time (ms)
 
 
Inc−S
Inc−T
 
 
Inc−S*
Inc−T*
4
5
6
7
8
10
3
10
4
10
5
10
6
k
time (ms)
 
 
Inc−S
Inc−T
 
 
Inc−S*
Inc−T*
4
5
6
7
8
10
3
10
4
10
5
k
time (ms)
 
 
Inc−S
Inc−T
 
 
Inc−S*
Inc−T*
4
5
6
7
8
10
3
10
4
10
5
k
time (ms)
 
 
Inc−S
Inc−T
 
 
Inc−S*
Inc−T*
(a) Flickr (invertedList)
(b) DBLP (invertedList)
(c) Tencent (invertedList)
(d) DBpedia (invertedList)
Figure 15: Effect of invertedList.
4
5
6
7
8
0
200
400
600
800
1000
k
time (ms)
 
 
Local
Dec
4
5
6
7
8
0
50
100
150
200
k
time (ms)
 
 
Local
Dec
4
5
6
7
8
0
2000
4000
6000
8000
k
time (ms)
 
 
Local
Dec
4
5
6
7
8
0
5000
10000
15000
k
time (ms)
 
 
Local
Dec
(a) Flickr
(b) DBLP
(c) Tencent
(d) DBpedia
Figure 16: Dec vs Local.
[20] R.-H. Li, J. X. Yu, and R. Mao. Efﬁcient core maintenance in
large dynamic graphs. TKDE, 2014.
[21] Y. Liu et al. Topic-link lda: joint models of topic and author
community. In ICML, 2009.
[22] R. M. Nallapati et al. Joint latent topic models for text and
citations. In KDD, 2008.
[23] M. Newman et al. Finding and evaluating community
structure in networks. Physical review E, 2004.
[24] Y. Ruan et al. Efﬁcient community detection in large
networks using content and links. In WWW, 2013.
[25] M. Sachan et al. Using content and interactions for
discovering communities in social networks. In WWW, 2012.
[26] S. B. Seidman. Network structure and minimum degree.
Social networks, 5(3):269–287, 1983.
[27] M. Sozio et al. The community-search problem and how to
plan a successful cocktail party. In KDD, 2010.
[28] Z. Xu et al. A model-based approach to attributed graph
clustering. In SIGMOD, 2012.
[29] Y. Fang et al. Effective community search for large attributed
graphs (technical report).
http://www.cs.hku.hk/research/techreps/
document/TR-2016-01.pdf.
[30] J. Yang et al. Community detection in networks with node
attributes. In ICDM, 2013.
[31] T. Yang et al. Combining link and content for community
detection: a discriminative approach. In KDD, 2009.
[32] J. X. Yu et al. Keyword search in databases. Synthesis
Lectures on Data Management, 2009.
[33] Y. Zhou et al. Graph clustering based on structural/attribute
similarities. VLDB, 2009.
13



## Page 14

APPENDIX
A.
PROOFS OF LEMMAS
LEMMA 1
(ANTI-MONOTONICITY). Given a graph G, a ver-
tex q ∈G and a set S of keywords, if there exists a subgraph Gk[S],
then there exists a subgraph Gk[S′] for any subset S′ ⊆S.
PROOF. Based on the deﬁnition of Gk[S], each vertex of Gk[S]
contains S. Consider a new keyword set S′ ⊆S. We can easily
conclude that, each vertex of Gk[S] contains S′ as well. Also, note
that q ∈Gk[S]. These two properties imply that there exists one
subgraph of G, namely Gk[S], with core number at least k, such
that it contains q and every vertex of it contains keyword set S′. It
follows that there exists such a subgraph with maximal size (i.e.,
Gk[S′]).
PROPOSITION 1. For any keyword set S, and vertex q, if Gk[S]
exists, then Gk[S] ⊆Gk[S′] for any subset S′ ⊆S.
PROOF. Since Gk[S] contains vertex q and every vertex in Gk[S]
contains S′ (due to S′ ⊆S), then Gk[S] ∪Gk[S′] also contains
vertex q and every vertex in it contains S′. In addition, the core
numbers of Gk[S] and Gk[S′] are at least k, it follows that the core
number of Gk[S] ∪Gk[S′] is at least k. Based on the deﬁnition
of Gk[S′], we have Gk[S] ∪Gk[S′] ⊆Gk[S′]. It follows that
Gk[S] ⊆Gk[S′].
LEMMA 2. Given two subgraphs Gk[S1] and Gk[S2] of a graph
G, for a new keyword set S′ generated from S1 and S2 (i.e., S′ =
S1 ∪S2), if Gk[S′] exists, then it must appear in a k- d
core with core
number at least
max{coreG[Gk[S1]], coreG[Gk[S2]]}.
(3)
PROOF. Since S′ is generated from S1 and S2, then S1 ⊆S′
and S2 ⊆S′. Based on Proposition 1, we have Gk[S′] ⊆Gk[S1].
With such a containment relationship, it follows that min{coreG[v]|
v ∈Gk[S1]} ≤min{coreG[v]|v ∈Gk[S′]}. Hence, the core
number of Gk[S′] is at least the core number of Gk[S1].
For-
mally, coreG[Gk[S1]] ≤coreG[Gk[S′]]. For the same reason,
coreG[Gk[S2]] ≤coreG[Gk[S′]].
It directly follows the lem-
ma.
LEMMA 3. Given a connected graph G(V, E) with n=|V | and
m=|E|, if m −n < k2−k
2
−1, there is no k- d
core in G.
PROOF. From Deﬁnition 1, we can easily conclude that, for any
speciﬁc k, a k- d
core has at least k+1 vertices. Since each vertex in a
speciﬁc k- d
core has at least k edges, the minimum number of edges
in a k- d
core is (k+1)k
2
.
Consider a connected graph, which contains a k- d
core and has the
minimum number of edges, where the k-core contains only k + 1
vertices and all the rest n−(k +1) vertices are connected with this
k- d
core. The total number of edges is
(k + 1)k
2
+ [n −(k + 1)] = m
(4)
By simple transformation, we can conclude that, if m −n <
k2−k
2
−1, there is no k- d
core in G.
LEMMA 4. Given two keyword sets S1 and S2, if Gk[S1] and
Gk[S2] exist, we have
Gk[S1 ∪S2] ⊆Gk[S1] ∩Gk[S2].
(5)
PROOF. Based on Proposition 1 and S1 ⊆S1 ∪S2, we have
Gk[S1 ∪S2] ⊆Gk[S1]. For the same reason we have Gk[S1 ∪
S2] ⊆Gk[S2]. It directly follows the lemma.
B.
DETAILS OF BASIC SOLUTIONS
Algorithms 5 and 6 present basic-g and basic-w respec-
tively. The input of basic-g is a graph G, a query vertex q, an
integer k and a set S. It ﬁrst generates a set, Ψ, of candidate key-
word sets, each of which contains a single keyword of S (line 2).
Then, it ﬁnds the k- d
core, Ck, containing q from the graph G. In
the while loop (lines 4-14), it ﬁrst initializes an empty set Φ (line
5), which is used to collect all the qualiﬁed keyword sets. Then for
each candidate keyword set S′ ∈Ψ, it ﬁnds G[S′] from Ck by con-
sidering the keyword constraint. After that, it ﬁnds Gk[S′] from
G[S′] (lines 7-8), and put it into Φ if Gk[S′] exists (lines 9-10).
After checking all the candidate keyword sets in Ψ, if there are at
least one qualiﬁed keyword sets in Φ, it generates a new set Ψ of
larger candidate keyword sets by calling GENECAND(Φ) (see Ap-
pendix C) and continues to checking longer candidate keyword sets
in next loop; otherwise, it stops and outputs all the communities of
the latest veriﬁed keyword sets as the target ACs.
Algorithm 5 Basic solution: basic-g
1: function QUERY(G, q, k, S)
2:
init Ψ using S;
3:
ﬁnd the k- d
core, Ck, containing q from G;
4:
while true do
5:
Φ ←∅;
6:
for each S′ ∈Ψ do
7:
ﬁnd G[S′] from Ck;
8:
ﬁnd Gk[S′] from G[S′];
9:
if Gk[S′] exists then
10:
Φ.add(S′);
11:
if Φ ̸= ∅then
12:
Ψ ←GENECAND(Φ);
13:
else
14:
break;
15:
output the communities of keyword sets in Φ;
Algorithm 6 presents the pseudocodes of basic-w. It follows
the main steps of basic-g, except that for each candidate key-
word set S′, it ﬁnds G[S′] from G directly, rather than from Ck.
Algorithm 6 Basic solution: basic-w
1: function QUERY(G, q, k, S)
2:
init Ψ using S;
3:
while true do
4:
Φ ←∅;
5:
for each S′ ∈Ψ do
6:
ﬁnd G[S′] from G;
7:
ﬁnd Gk[S′] from G[S′];
8:
if Gk[S′] exists then
9:
Φ.add(S′);
10:
if Φ ̸= ∅then
11:
Ψ ←GENECAND(Φ);
12:
else
13:
break;
14:
output the communities of keyword sets in Φ;
C.
CANDIDATE GENERATION
Given a set Φ of qualiﬁed keyword sets, Algorithm 7 generates
new candidate keyword sets incrementally by linking each pair of
keyword sets. We ﬁrst initialize Ψ as an empty set (line 2). Then
for each pair, Si and Sj, of keyword sets in Φ, we sort their key-
words. If they differ only at the last keyword, then we generate a
new keyword set S′=Si ∪Sj, by a union operation (lines 3-6). Ac-
cording to Lemma 1, if any subset of S′ does not appear in Φ, we
14



## Page 15

prune S′; otherwise, we regard it as a candidate and add it into Ψ
(lines 7-8). Finally, we return Ψ as the results (line 9).
Algorithm 7 Generate candidate keyword sets
1: function GENECAND(Φ)
2:
Ψ ←∅;
3:
for each Si ∈Φ do
4:
for each Sj ∈Φ do
5:
if Si and Sj differs at the last keyword then
6:
initialize S′=Si ∪Sj;
7:
if S′ cannot be pruned by Lemma 1 then
8:
Ψ.add(S′);
9:
return Ψ;
D.
ANCHORED UNION-FIND
Algorithm 8 presents the four functions of the anchored union-
ﬁnd (AUF) data structure.
Algorithm 8 Functions on the AUF data structure
1: function MAKESET(x)
2:
x.parent ←x;
3:
x.rank ←0;
4:
x.anchor ←x;
5: function FIND(x)
6:
if x.parent=x then
7:
x.parent ←FIND(x.parent);
8:
return x.parent;
9: function UNION(x, y)
10:
xRoot ←FIND(x);
11:
yRoot ←FIND(y);
12:
if xRoot=yRoot then return ;
13:
if xRoot.rank < yRoot.rank then
14:
xRoot.parent ←yRoot;
15:
else if xRoot.rank > yRoot.rank then
16:
yRoot.parent ←xRoot;
17:
else
18:
yRoot.parent ←xRoot;
19:
xRoot.rank ←xRoot.rank + 1;
20: function UPDATEANCHOR(x, coreG[ ], y)
21:
xRoot ←FIND(x);
22:
if coreG[xRoot.anchor] > coreG[y] then
23:
xRoot.anchor ←y;
The functions FIND and UNION are exactly the same as that of
the classical union-ﬁnd data structure [1]. For function MAKESET,
the only change made on the classical MAKESET is that, it adds a
line of code for initializing x.anchor as x (line 4). The function
UPDATEANCHOR is used to update the anchor vertex of x’s repre-
sentative vertex. It ﬁrst ﬁnds x’s representative vertex by calling
FIND (line 21). Then, if the core number of x’ representative vertex
is larger than that of the current input vertex y, it updates the anchor
vertex of x’s representative vertex as y.
Complexity analysis. The time complexities of functions FIND
and UNION are O(α(n)) [1], where α(n) is less than 5 for al-
l practical values of n. In function MAKESET, since initializing
x.anchor can be done in O(1), the time complexity of MAKESET
is still O(1). In function UPDATEANCHOR, as FIND can be com-
pleted in O(α(n)) and updating anchor can be completed in O(1),
the total time cost of function UPDATEANCHOR is O(α(n)).
E.
DETAILSOFTHEADVANCEDMETHOD
Algorithm 9 presents the advanced method. Similar with basic
method, we ﬁrst conduct k-decomposition (line 2). Then, for each
Algorithm 9 Index construction: advanced
1: function BUILDINDEX(G(V, E))
2:
coreG[ ] ←k-core decomposition on G;
3:
for each v ∈V do MAKESET(v);
4:
put vertices into sets V0, V1, · · · , Vkmax;
5:
k ←kmax, map ←∅;
6:
while k ≥0 do
7:
V ′ ←∅;
8:
for each v ∈Vk do V ′.add(FIND(v));
9:
compute connected components for Vk ∪V ′;
10:
for each component with vertex set Ci do
11:
create a node pi using (k, {Ci −V ′});
12:
for each v ∈{Ci −V ′} do
13:
map.add(v, pi);
14:
for each u ∈v’s neighbor vertices do
15:
if coreG[u] ≥coreG[v] then
16:
UNION(u, v);
17:
if coreG[u] > coreG[v] then
18:
uRoot ←FIND(u);
19:
uAnchor ←uRoot.anchor;
20:
p′ ←map.get(uAnchor);
21:
add p′ to p’s child List;
22:
vRoot ←FIND(v);
23:
if coreG[vRoot.anchor] > coreG[v] then
24:
UPDATEANCHOR(vRoot, coreG[ ], v);
25:
k ←k −1;
26:
build the root node root;
27:
build an inverted list for each tree node;
28:
return root.
vertex, we initialize an AUF tree node (line 3). We group all the
vertices into sets (line 4), where set Vk contains vertices with core
numbers being exactly k (line 5). Next, we initialize k as kmax
and the vertex-node map map, where the key is a vertex and the
value is a CL-tree node whose vertex set contains this vertex. In
the while loop (lines 6-25), we ﬁrst ﬁnd the set V ′ of the represen-
tatives for vertices in Vk, then compute the connected components
for vertex set Vk ∪V ′ (lines 7-9). Next, we create a node pi for
each component (lines 10-11). For each vertex v ∈{Ci −V ′}, we
add a pair (v, pi) to the map (lines 12-13). Then for each of v’s
neighbor, u, if its core number is at least coreG[v], we link u and v
together in the AUF by a UNION operation (lines 14-16), and ﬁnd
pi’s child nodes using the anchor of the AUF tree (lines 17-21). Af-
ter vertex v has been added into the CL-tree, we update the anchor
(lines 22-24). Then we move to the upper level in next loop (line
25). After the while loop, we build the root node of the CL-tree
(line 26). Finally, we build the inverted list for each tree node and
obtain the built index (lines 27-28).
Complexity analysis. In Algorithm 9, lines 1-3 can be com-
pleted in O(m) (We assume m¿n). In the while loop, the number
of operations on each vertex and its neighbors are constant, and
each can be done in O(α(n)), where α(n) is the inverse Acker-
mann function. The keyword inverted lists of all the tree nodes
can be computed in O(n · bl). Therefor, the CL-tree can be built in
O(m·α(n)+n·bl). The space cost is O(m+n·bl), as maintaining
an AUF takes O(n).
F.
INDEX MAINTENANCE
For CL-tree maintenance, we note that on our largest graph DB-
pedia (|V |=8M, |E|=72M), the CL-tree can be constructed in 30
seconds. A simple solution is to rebuild the CL-tree for batches of
graph updates periodically (say, every 15 minutes).
We now sketch an incremental solution which updates the CL-
tree without rebuilding it. We consider two actions that affect the
15



## Page 16

CL-tree: (1) insertion or deletion of a keyword on a vertex’s key-
word set; and (2) insertion or removal of an edge on the graph G.
1. Keyword update. In the Advanced index construction method
(Sec 5.2.2), we have built a vertex-node map, where each vertex is
mapped to a CL-tree node. To insert a new keyword for a vertex v,
we can ﬁrst use the map to ﬁnd the CL-tree node, which contains
v, and then insert the keyword and vertex ID into the associated
invertedList. To remove a keyword of a vertex, we can ﬁrst ﬁnd
the CL-tree node, then look for the invertedList containing the key-
word, and remove the vertex ID and/or keyword from the list. Note
that only nodes that contain v need to be considered. Since the CL-
tree is compressed, only the invertedList of a single CL-tree node
containing v needs to be updated.
2. Edge update. The insertion or removal of an edge affects the
core number of vertices in G. Notice that the structural cohesive-
ness of an AC follows the k-core deﬁnition. Therefore, it is possi-
ble to adopt the techniques that have been developed for updating
k-cores. Here we consider [20], which presents an efﬁcient k-core
maintenance algorithm. As discussed in [20], given that a new edge
(u, v) is inserted to G, only an vertex whose core number is c or
c + 1 will be affected, where c is the minimum of the core num-
bers of u and v in G (i.e., c = min{coreG[u], coreG[v]}). Based
on this result, a possible CL-tree maintenance solution involves (1)
ﬁnding the CL-tree nodes pu and pv containing u and v; (2) travers-
ing the subtrees rooted at pu and pv and stopping at CL-tree nodes
with core number c + 2 or more; (3) for each CL-tree node visited,
update its links to child nodes. These steps only touches a smal-
l fraction of the CL-tree. The case of deletion can be done in a
similar manner. We plan to study this solution in more detail, and
conduct extensive experimental evaluation.
G.
VARIANTS OF ACQ PROBLEM
In this section, we formally deﬁne two typical variants in Sec-
tion G.1. Then we present the algorithms for these variants in Sec-
tion G.2, and show the experimental results ﬁnally in Section G.3.
G.1
Variant Deﬁnitions
VARIANT 1. Given a graph G, a positive integer k, a vertex
q ∈V and a predeﬁned keyword set S, return a subgraph Gq, the
following properties hold:
1. Connectivity. Gq ⊆G is connected and contains q;
2. Structure cohesiveness. ∀v ∈Gq, degGq(v) ≥k;
3. Keyword cohesiveness. ∀v ∈Gq, S ⊆W(v).
Variant 1 can be applied to applications, which need communi-
ties having speciﬁc keyword constraints.
VARIANT 2. Given a graph G, a positive integer k, a vertex
q ∈V , a predeﬁned keyword set S, and a threshold θ ∈[0,1],
return a subgraph Gq, the following properties hold:
1. Connectivity. Gq ⊆G is connected and contains q;
2. Structure cohesiveness. ∀v ∈Gq, degGq(v) ≥k;
3. Keyword cohesiveness. ∀v ∈Gq, it has at least |S| × θ
keywords in S.
In Variant 2, the keyword cohesiveness is relaxed. This can be
applied for cases when the keyword information is weak. We illus-
trate all the variants in Example 7.
EXAMPLE 7. Consider Figure 3(a). Let q=A and k=2. For
Variant 1, if the predeﬁned keyword set is {x}, then the vertex set
{A, B, C, D} forms the target AC. For Variant 2, if the predeﬁned
keyword set is {x, y} and the threshold is 50%, then the vertex set
{A, B, C, D, E} forms the target AC.
G.2
Algorithms of Variants
1. Variant 1. In line with Problem 1, we ﬁrst introduce the
basic solutions without index, which are extended naturally from
basic-g and basic-w, and are denoted by basic-g-v1 and
basic-w-v1 respectively. Their details pseudocodes are present-
ed in Algorithms 10 and 11.
Algorithm 10 Query algorithm: basic-g-v1
1: function QUERY(G, q, k, S)
2:
ﬁnd the k- d
core, Ck, containing q from G;
3:
collect a set V ′ of vertices containing S from Ck;
4:
ﬁnd G[S] from the subgraph induced by V ′;
5:
ﬁnd Gk[S] from G[S];
6:
output Gk[S] as the target AC.
Algorithm 11 Query algorithm: basic-w-v1
1: function QUERY(G, q, k, S)
2:
collect a set V ′ of vertices containing S from G;
3:
ﬁnd G[S] from the subgraph induced by V ′;
4:
ﬁnd Gk[S] from G[S];
5:
output Gk[S] as the target AC.
Algorithm 12 presents the index based algorithm, SW, for Vari-
ant 1. We ﬁrst apply core-locating to ﬁnd node rk, whose
corresponding k- d
core contains q, from CL-tree (line 1). Then we
traverse the subtree rooted at rk, and collect a set V ′ of vertices
containing S by applying keyword-checking. Next, we ﬁnd
G[S] from the subgraph induced by vertices in V ′ (line 3), and ﬁnd
Gk[S] from G[S] (line 4). Finally, we output Gk[S] as the target
AC, if it exists (line 5).
Algorithm 12 Query algorithm: SW
1: function QUERY(G, root, q, k, S)
2:
ﬁnd the node rk from the CL-tree index;
3:
traverse the subtree rooted at rk and collect a set V ′ of
vertices containing S by intersecting the inverted lists;
4:
ﬁnd G[S] from the subgraph induced by V ′;
5:
ﬁnd Gk[S] from G[S];
6:
output Gk[S] as the target AC.
2. Variant 2. We adapt the three algorithms of Variant 1 for
answering the query of Variant 2. We denote the adapted algorithms
by basic-g-v2, basic-w-v2 and SWT (search by keywords
with threshold constraint) respectively. The main adaptation is that,
for the lines of codes on collecting vertices containing S, i.e., line 3
in Algorithm 10, line 2 in Algorithm 11, and line 3 in Algorithm 12,
we relax the constraint such that each collected vertex only needs
to share at least |S| × θ keywords in S. Then we ﬁnd the target AC
from the subgraph induced by these vertices.
G.3
Experiments on Variants
1. Case study of Variants 1 and 2. We search Jiawei Han’s
communities with explicit AC-label constraints in Variants 1 and 2.
We consider two keyword sets, i.e., S1={stream, classiﬁcation}
and S2={cube, information, cluster}. For Variant 1, we can only
obtain a community for S1 (see Figure 18(a)), and no communities
for S2. Note that the captions indicate the shared keywords of the
16



## Page 17

1
3
5
7
9
10
0
10
2
the number of keywords in S
time (ms)
 
 
basic−g−v1
basic−w−v1
SW
1
3
5
7
9
10
1
10
2
10
3
the number of keywords in S
time (ms)
 
 
basic−g−v1
basic−w−v1
SW
1
3
5
7
9
10
1
10
2
10
3
the number of keywords in S
time (ms)
 
 
basic−g−v1
basic−w−v1
SW
1
3
5
7
9
10
1
10
2
10
3
10
4
the number of keywords in S
time (ms)
 
 
basic−g−v1
basic−w−v1
SW
(a) Flickr (Variant 1)
(b) DBLP (Variant 1)
(c) Tencent (Variant 1)
(d) DBpedia (Variant 1)
0.2
0.4
0.6
0.8
1.0
10
1
10
2
10
3
the value of θ
time (ms)
 
 
basic−g−v2
basic−w−v2
SWT
0.2
0.4
0.6
0.8
1.0
10
1
10
2
10
3
the value of θ
time (ms)
 
 
basic−g−v2
basic−w−v2
SWT
0.2
0.4
0.6
0.8
1.0
10
2
10
3
10
4
the value of θ
time (ms)
 
 
basic−g−v2
basic−w−v2
SWT
0.2
0.4
0.6
0.8
1.0
10
2
10
3
10
4
the value of θ
time (ms)
 
 
basic−g−v2
basic−w−v2
SWT
(e) Flickr (Variant 2)
(f) DBLP (Variant 2)
(g) Tencent (Variant 2)
(h) DBpedia (Variant 2)
Figure 17: Efﬁciency results of Variants of ACQ problem.
communities. While for Variant 2 (θ=0.6), we can obtain two com-
munities (see Figures 18(a) and 18(b)). This implies that, for Vari-
ant 2, although we cannot ﬁnd a community with AC-label being
exactly S2, we still can ﬁnd a community, in which each member
contains at least 60% percentage of keywords of the input query
keyword set.
Jiawei Han
Charu C. Aggarwal
Latifur Khan
Mohammad M. Masud
Clay Woolam
Nikunj C. Oza
Jing Gao
(a) {stream, classiﬁcation}
Jiawei Han
Ashok N. Srivastava
Yizhou Sun
Chengxiang Zhai
Binbin Liao
Yintao Yu
Duo Zhang
Cindy Xide Lin
(b) {cube, information}
Figure 18: Jiawei Han’s communities on Variants 1 and 2.
2. Effect of |S| in Variant 1. We consider query vertices having
at least 9 keywords. For each of them, we randomly select 1, 3,
5, 7 and 9 keywords to form the query keyword sets, and answer
the query of Variant 1 using basic-g-v1, basic-w-v1 and
SW. Figures 17(a)-17(d) show their efﬁciency. We can see that SW
outperforms the basic solutions consistently. Also, the performance
gap increases between SW and basic solutions as |S| increases. This
is because it uses the CL-tree index.
3. Effect of θ in Variant 2. For each query vertex, we ran-
domly select 10 keywords to form set S, set θ as 0.2, 0.4 0.6, 0.8
and 1.0, and answer the query of Variant 2 using basic-g-v2,
basic-w-v2 and SWT. Figures 17(e)-17(h) show their efﬁciency.
Similar with Variant 1, we can see that SWT performs the best, as it
uses the CL-tree index.
17


