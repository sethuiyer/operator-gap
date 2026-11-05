# Milestone A: Uniform All-Primes Approximation for Mighty-K Weights

**Status.** This note proves the all-primes uniform approximation theorem for the
prime-adapted Mighty-K construction. It does **not** prove the Riemann
hypothesis. The resulting \(\Psi_K\) criterion is equivalent to RH only after
combining the approximation theorem with the classical \(\psi\)-error
criterion; that equivalence is inherited, not intrinsic to the permutation
construction.

The constants below are deliberately conservative. The important output is the
polynomial schedule \(K(X)=X^7\) and the uniform convergence
\(\Psi_K\to\psi\).

**Problem (Milestone A).** For each prime \(p\), construct the prime-adapted
centered concatenation \(Y_{K,p}\), prove a uniform lower bound for the number
of active adjacent pairs, and deduce an explicit Fourier estimate for
\(A_{K,p,r}(j)\). Then choose a schedule \(K(X)\) such that the
prime-power weights \(\Lambda_K(n)\) satisfy

\[
\sup_{2\le x\le X}
\frac{|\Psi_K(x)-\psi(x)|}{\sqrt{x}\log^2(2x)}
\longrightarrow0.
\]

Finally, record the RH equivalence inherited from the classical
\(\psi\)-criterion. This note proves the approximation theorem; it does not
prove RH or the intrinsic Mighty-K equivalence.

---

## 0. Definitions and notation

Let \(p\) be prime and set

\[
b=b_p=p^2+1\ge 5,\qquad m=K-1\ge 2.
\]

For \(n\ge1\), let \(d_b(n)\) be the number of base-\(b\) digits of \(n\), so

\[
d_b(n)=d\quad\Longleftrightarrow\quad b^{d-1}\le n\le b^d-1.
\]

For a permutation \(\pi=(n_1,\dots,n_m)\) of \(1,\dots,m\), let
\(C_{K,b}(\pi)\) be the integer obtained by concatenating the base-\(b\)
representations of \(n_1,\dots,n_m\). Define the centered value

\[
Y_{K,p}(\pi)=\frac{C_{K,b}(\pi)-m(m+1)/2}{p^2}.
\]

This is an integer because \(b\equiv1\pmod{p^2}\).

For \(r\ge1\) and an integer \(j\), define the Fourier coefficient

\[
A_{K,p,r}(j)
=\mathbb E_{\pi\in S_m}
\exp\!\left(\frac{2\pi i\,j\,Y_{K,p}(\pi)}{p^r}\right).
\]

For a pair of distinct labels \(a,c\in\{1,\dots,m\}\), define

\[
\Delta_p(a,c)=a\,d_b(c)-c\,d_b(a)\pmod p.
\]

Call \(\{a,c\}\) **active** if \(\Delta_p(a,c)\ne0\pmod p\).

For a random adjacent matching of the \(m\) positions (pairs
\((1,2),(3,4),\dots\), with one unmatched position if \(m\) is odd), let \(H\)
be the number of active pairs.

The local shell coefficients are

\[
c_{K,p}(n)=\frac{p}{p-1}\,p^n\,\Pr\bigl(v_p(Y_{K,p})=n\bigr),
\qquad n\ge0,
\]

and the local logarithmic coefficients \(\lambda_{K,p}(a)\) are defined by

\[
z\frac{d}{dz}\log \widetilde Z_{K,p}(z)
=\sum_{a\ge1}\lambda_{K,p}(a)z^a,
\qquad
\widetilde Z_{K,p}(z)
=\frac{1}{c_{K,p}(0)}
\sum_{n\ge0}c_{K,p}(n)z^n.
\]

---

## 1. Theorem 1: uniform cross-tier active-pair bound

### Statement

For every prime \(p\), every \(b=p^2+1\), and every \(m\ge2\),

\[
\boxed{
\Pr_{a\ne c}\bigl(\Delta_p(a,c)\ne0\bigr)\ge\frac1{5b}
=\frac1{5(p^2+1)}.
}
\tag{1.1}
\]

The probability is over a uniformly random unordered pair of distinct labels
in \(\{1,\dots,m\}\).

### Two elementary lemmas

**Lemma 1.1 (different residues in a consecutive interval).**
Let \(I\) be a set of \(t\ge2\) consecutive integers. The fraction of unordered
pairs \(\{x,y\}\subset I\) with \(x\not\equiv y\pmod p\) is at least
\(1-1/p\).

*Proof.* Write \(t=qp+r\) with \(0\le r<p\). Among the \(t\) integers, \(r\)
residue classes occur \(q+1\) times and \(p-r\) occur \(q\) times. The number of
same-residue pairs is

\[
r\binom{q+1}{2}+(p-r)\binom q2
=\frac{q(t+r-p)}2
\le\frac{q(t-1)}2.
\]

Dividing by \(\binom t2=t(t-1)/2\), the same-residue fraction is at most
\(q/t\le1/p\). Hence the different-residue fraction is at least \(1-1/p\).
\(\square\)

**Lemma 1.2 (nonzero residues in a prefix starting at \(1\)).**
Let \(I\) be a set of \(t\ge1\) consecutive integers whose first element is
\(\equiv1\pmod p\). Then at least half of the elements of \(I\) are nonzero
modulo \(p\).

*Proof.* Write \(t=qp+r\), \(0\le r<p\). If \(r=0\), exactly \(q(p-1)\) of the
\(qp\) elements are nonzero, a fraction \((p-1)/p\ge1/2\). If \(r\ge1\), the
first \(r\) residues of the final partial cycle are \(1,2,\dots,r\), all
nonzero, so the nonzero count is \(q(p-1)+r\). Its fraction of \(t=qp+r\) is at
least \(1/2\) because

\[
2(q(p-1)+r)-(qp+r)=q(p-2)+r\ge0.
\]

\(\square\)

### Proof of Theorem 1

Let \(d=d_b(m)\).

**Case \(d=1\).** All labels have digit length \(1\). Hence
\(\Delta_p(a,c)=a-c\pmod p\), and a pair is active exactly when its residues
differ. Lemma 1.1 gives

\[
\Pr(\text{active})\ge1-\frac1p\ge\frac12\ge\frac1{5b},
\]

since \(b\ge5\).

Now assume \(d\ge2\). Put

\[
Q=(b-1)b^{d-2},\qquad N=b^{d-1}-1,\qquad t=m-N.
\]

The labels \(1,\dots,N\) have digit length \(<d\); the labels \(N+1,\dots,m\)
form the partial top tier of digit length \(d\), of size \(t\). The tier of
digit length \(d-1\) is complete and has size

\[
b^{d-1}-b^{d-2}=b^{d-2}(b-1)=Q.
\]

We have \(1\le t\le bQ\), and

\[
\frac NQ
=\frac{b}{b-1}-\frac{1}{(b-1)b^{d-2}}
<\frac54
\tag{1.2}
\]

because \(b\ge5\).

**Case A: \(p\nmid(d-1)\).**

*A1: \(t\le Q\).* The completed tier of length \(d-1\) has exactly \(Q/p\)
labels in each residue class modulo \(p\). Since \(d-1\) is a unit modulo \(p\),
two labels in this tier are active exactly when their residues differ. The
number of active pairs inside the tier is

\[
\binom Q2-p\binom{Q/p}{2}
=\frac12Q^2\left(1-\frac1p\right).
\]

Using \(m=N+t\le\frac54Q+Q=\frac94Q\), we get

\[
\Pr(\text{active})
\ge\frac{Q^2(1-1/p)}{m(m-1)}
\ge\frac{16(1-1/p)}{81}
\ge\frac8{81}.
\tag{1.3}
\]

*A2: \(t>Q\) and \(p\nmid d\).* The top tier has \(t\) labels, all of digit
length \(d\). Since \(d\) is a unit modulo \(p\), a pair inside this tier is
active exactly when its residues differ. Lemma 1.1 gives at least
\(\frac12\binom t2\) active pairs. Using \(m=N+t<\frac54t+t=\frac94t\),

\[
\Pr(\text{active})
\ge\frac{t(t-1)}{2m(m-1)}
>\frac{8}{81}\cdot\frac{t-1}{t}
\ge\frac4{81}.
\tag{1.4}
\]

*A3: \(t>Q\) and \(p\mid d\).* The top tier starts at \(b^{d-1}\equiv1\pmod p\).
By Lemma 1.2, at least half of its labels are nonzero modulo \(p\). Every such
label \(a\) forms an active pair with every label \(c\) in the completed tier,
because

\[
\Delta_p(a,c)\equiv a(d-1)\not\equiv0\pmod p.
\]

Thus there are at least \(tQ/2\) active cross pairs. With
\(u=t/Q\in(1,b]\),

\[
\Pr(\text{active})
\ge\frac{tQ}{m(m-1)}
>\frac{tQ}{m^2}
\ge\frac{u}{(5/4+u)^2}.
\tag{1.5}
\]

The function \(f(u)=u/(5/4+u)^2\) increases on \((0,5/4)\) and decreases on
\((5/4,\infty)\). Since \(b\ge5\), its minimum on \((1,b]\) is at \(u=b\).
Moreover,

\[
f(b)=\frac{b}{(b+5/4)^2}\ge\frac4{9b}
\]

because \(9b^2\ge4(b+5/4)^2\) for \(b\ge5\). Hence
\(\Pr(\text{active})\ge4/(9b)\).

**Case B: \(p\mid(d-1)\).** Then \(d\ge3\), and both \(d\) and \(d-2\) are
nonzero modulo \(p\). The completed tier of length \(d-1\) has \(Q\) labels,
balanced across residues modulo \(p\); at least \(Q/2\) of them are nonzero.
Every nonzero \(a\) in this tier forms an active pair with every label in a
neighboring tier of digit length \(d\) or \(d-2\), since

\[
\Delta_p(a,c)\equiv a\,d_b(c)\not\equiv0\pmod p.
\]

*B1: \(t\ge Q/b\).* Use the top tier. There are at least \((Q/2)t\) active
cross pairs, so

\[
\Pr(\text{active})
\ge\frac{Qt}{m(m-1)}
>\frac{Qt}{m^2}
\ge\frac{u}{(5/4+u)^2},
\qquad u=\frac tQ\ge\frac1b.
\tag{1.6}
\]

On \([1/b,b]\), the minimum of \(f\) is at an endpoint. Both endpoints give at
least \(4/(9b)\):

\[
f(1/b)=\frac{16b}{(5b+4)^2}\ge\frac4{9b}
\quad\Longleftrightarrow\quad
36b^2\ge(5b+4)^2,
\]

which holds for \(b\ge4\); and \(f(b)\ge4/(9b)\) as above.

*B2: \(t<Q/b\).* Use the completed tier of length \(d-2\), which has size
\(Q/b\). There are at least

\[
\frac Q2\cdot\frac Qb=\frac{Q^2}{2b}
\]

active cross pairs. Since

\[
m=N+t<\left(\frac54+\frac1b\right)Q\le\frac{29}{20}Q,
\]

we obtain

\[
\Pr(\text{active})
\ge\frac{Q^2}{b\,m(m-1)}
>\frac{Q^2}{b\,m^2}
\ge\frac{400}{841b}
>\frac4{9b}.
\tag{1.7}
\]

The cases A1–A3 and B1–B2 exhaust all \(m\). Finally, for \(b\ge5\),

\[
\min\left\{\frac8{81},\frac4{81},\frac4{9b}\right\}
\ge\frac1{5b},
\]

because \(4/81\ge1/(5b)\) for \(b\ge4.05\), \(8/81>4/81\), and
\(4/(9b)\ge1/(5b)\). This proves (1.1). \(\square\)

### Consequence for the mean active count

A random adjacent matching contributes \(\lfloor m/2\rfloor\) unordered pairs,
and each pair is marginally uniform among all unordered pairs of distinct
labels. By linearity,

\[
\mathbb E H
=\left\lfloor\frac m2\right\rfloor\Pr(\text{active})
\ge\left\lfloor\frac m2\right\rfloor\frac1{5b}
\ge\frac{m}{15b}
\tag{1.8}
\]

for \(m\ge2\).

---

## 2. Theorem 2: explicit all-primes Fourier decay

### Statement

For every prime \(p\), every \(r\ge1\), and every nonzero character
\(j\pmod{p^r}\),

\[
\boxed{
|A_{K,p,r}(j)|
\le
\exp\!\left(-\frac{m}{7200b^2}\right)
+
\exp\!\left(-\frac{m}{15bp^{2r}}\right).
}
\tag{2.1}
\]

### Proof

Pair adjacent positions as in the definition of \(H\). The pair orientations
are independent fair bits once the unordered pairs are fixed.

**Concentration.** Swapping two labels changes the activity of at most two
position-pairs. Exposing a uniform permutation one entry at a time therefore
gives Doob martingale differences of conditional range at most \(2\). Hoeffding
gives, for \(0<u<\mathbb E H\),

\[
\Pr(H\le \mathbb E H-u)
\le\exp\!\left(-\frac{u^2}{2m}\right).
\]

Taking \(u=\frac12\mathbb E H\) and using (1.8),

\[
\Pr\!\left(H<\frac{m}{30b}\right)
\le\Pr\!\left(H<\frac12\mathbb E H\right)
\le
\exp\!\left(-\frac{(\mathbb E H)^2}{8m}\right)
\le
\exp\!\left(-\frac{m}{1800b^2}\right).
\tag{2.2}
\]

This is stronger than the first term in (2.1).

**Orientation average.** Condition on the unordered pairs. Write
\(Y_{K,p}=y_0+\sum_e\varepsilon_e\Delta Y_e\), where \(\varepsilon_e=\pm1\) and
\(\Delta Y_e\) is the change produced by reversing pair \(e\). The suffix
length after a pair is unchanged by reversing that pair, so \(\Delta Y_e\) is
fixed by the unordered-pair data. For an active pair,
\(\Delta Y_e\not\equiv0\pmod p\).

The conditional characteristic function is therefore

\[
\prod_e \cos\!\left(\frac{\pi j\Delta Y_e}{p^r}\right)
\]

up to a fixed unimodular factor. For a primitive character \(j\), \(j\Delta
Y_e\) is a unit modulo \(p^r\) for every active \(e\). Hence

\[
\left|\cos\!\left(\frac{\pi j\Delta Y_e}{p^r}\right)\right|
\le\cos\!\left(\frac{\pi}{p^r}\right)
\le e^{-2/p^{2r}}.
\tag{2.3}
\]

The last inequality follows from \(-\log\cos x\ge x^2/2\) for \(|x|\le\pi/2\)
and \(x^2/2=\pi^2/(2p^{2r})\ge2/p^{2r}\).

Multiplying over the \(H\) active pairs gives modulus at most
\(e^{-2H/p^{2r}}\). Therefore, on the event \(H\ge m/(30b)\),

\[
\left|\mathbb E\!\left[
e^{2\pi i jY_{K,p}/p^r}\mid\text{unordered pairs}
\right]\right|
\le
e^{-m/(15bp^{2r})}.
\tag{2.4}
\]

Combining (2.2) and (2.4),

\[
|A_{K,p,r}(j)|
\le
e^{-m/(7200b^2)}
+
e^{-m/(15bp^{2r})}.
\]

**Nonprimitive characters.** If \(j\pmod{p^r}\) is nonprimitive, it factors
through a character modulo \(p^s\) with \(s<r\). The bound (2.1) at depth \(s\)
has second exponent \(-m/(15bp^{2s})\), which is at most
\(-m/(15bp^{2r})\). Hence the depth-\(r\) bound applies. \(\square\)

---

## 3. Theorem 3: uniform prime-counting approximation

### Statement

Define

\[
\Lambda_K(p^a)=(\log p)\lambda_{K,p}(a),
\qquad
\Lambda_K(n)=0
\text{ if }n\text{ is not a prime power},
\]

and

\[
\Psi_K(x)=\sum_{n\le x}\Lambda_K(n).
\]

Take

\[
K(X)=\lceil X^7\rceil.
\]

Then there is an absolute \(X_0\) such that for every \(X\ge X_0\),

\[
\boxed{
\sup_{2\le x\le X}
|\Psi_{K(X)}(x)-\psi(x)|
\le
4X^6\log X
\left(
e^{-X^3/22500}
+
e^{-X/37.5}
\right).
}
\tag{3.1}
\]

The constant \(4\) is not optimized; it can be enlarged to absorb finitely many
small \(X\).

Consequently,

\[
\boxed{
\sup_{2\le x\le X}
\frac{|\Psi_{K(X)}(x)-\psi(x)|}
{\sqrt{x}\log^2(2x)}
\longrightarrow0.
}
\tag{3.2}
\]

### Proof

Let \(K=K(X)\), \(m=K-1\), and let \(p^a\le X\) be a prime power. Put
\(r=a+1\). Then

\[
p^r=p^{a+1}\le X^2,
\tag{3.3}
\]

\[
b^2=(p^2+1)^2\le (X^2+1)^2\le\frac{25}{16}X^4,
\tag{3.4}
\]

and

\[
bp^{2r}=(p^2+1)p^{2a+2}\le (X^2+1)X^4\le\frac54X^6
\tag{3.5}
\]

for \(X\ge2\).

Since \(m=K-1\ge X^7/2\) for large \(X\), Theorem 2 gives, uniformly in
\(p^a\le X\),

\[
|A_{K,p,r}(j)|
\le
e^{-X^3/22500}
+
e^{-X/37.5}.
\tag{3.6}
\]

**Total-variation bound.** Let \(\mu_{K,p,r}\) be the law of
\(Y_{K,p}\pmod{p^r}\), and \(U_{p^r}\) the uniform law. Since \(p^r\le X^2\),
the crude Fourier bound gives

\[
\delta_X
:=
\|\mu_{K,p,r}-U_{p^r}\|_{\mathrm{TV}}
\le
\frac{X^2}{2}
\left(
e^{-X^3/22500}
+
e^{-X/37.5}
\right).
\tag{3.7}
\]

**Shell coefficients.** For \(0\le n\le a\), the shell
\(\{v_p(Y_{K,p})=n\}\) is a single measurable set modulo \(p^r\), so (3.7)
controls its probability by \(\delta_X\). Since

\[
c_{K,p}(n)=\frac{p}{p-1}p^n\Pr(v_p(Y_{K,p})=n),
\]

and the Haar shell probability is \((1-1/p)p^{-n}\), we get

\[
|c_{K,p}(n)-1|
\le
\frac{p}{p-1}p^n\delta_X
\le
2X\delta_X.
\tag{3.8}
\]

**Logarithmic coefficients.** For fixed \(p\), set

\[
Z_a(z)=\sum_{n=0}^{a}c_{K,p}(n)z^n,
\qquad
H_a(z)=1+z+\cdots+z^a,
\qquad
E_a=Z_a-H_a.
\]

On \(|z|=1/4\),

\[
|E_a(z)|
\le\sum_{n=0}^a 2X\delta_X4^{-n}
\le\frac83X\delta_X,
\]

and

\[
|E_a'(z)|
\le\sum_{n=1}^a 2X\delta_X\,n4^{-(n-1)}
=\frac{32}{9}X\delta_X.
\]

Also \(|H_a(z)|\ge3/4\) for \(a\ge1\) (indeed \(\ge5/4\)), and

\[
|H_a'(z)|
\le\sum_{n=1}^a n4^{-(n-1)}
=\frac{16}{9}.
\]

Assume \(X\delta_X\le3/64\). Then \(|E_a(z)|\le1/8\), so

\[
|Z_a(z)|
\ge|H_a(z)|-|E_a(z)|
\ge\frac34-\frac18
=\frac58.
\]

Rouché's theorem (or the same estimate) shows that \(Z_a\) has no zeros in
\(|z|\le1/4\), since \(H_a\) has none.

Set

\[
D_a(z)
=z\left(\frac{Z_a'(z)}{Z_a(z)}-\frac{H_a'(z)}{H_a(z)}\right).
\]

The preceding bounds give

\[
|D_a(z)|
\le\frac14\left(
\frac{|E_a'|}{|Z_a|}
+
\frac{|E_a||H_a'|}{|Z_a||H_a|}
\right)
<4X\delta_X.
\]

Since the logarithmic derivative of \(H_a\) has coefficient \(1\) in every
degree \(1\le j\le a\), Cauchy's coefficient estimate gives

\[
|\lambda_{K,p}(a)-1|
\le4^a\cdot4X\delta_X
=4^{a+1}X\delta_X
\le4X^3\delta_X,
\tag{3.9}
\]

because \(4^a\le X^2\) for \(p^a\le X\).

**Summation over prime powers.** For \(x\le X\),

\[
|\Psi_K(x)-\psi(x)|
\le
\sum_{p^a\le X}\log p\,|\lambda_{K,p}(a)-1|
\le
4X^3\delta_X\sum_{n\le X}\log n.
\]

The elementary bound \(\sum_{n\le X}\log n\le X\log X\) gives the sharper
estimate

\[
|\Psi_K(x)-\psi(x)|
\le
4X^4\log X\,\delta_X
\le
2X^6\log X
\left(
e^{-X^3/22500}
+
e^{-X/37.5}
\right).
\]

The theorem is stated with the conservative constant \(4\); it follows by
using the weaker coefficient bound \(8X^3\delta_X\), which gives
\(8X^4\log X\,\delta_X\) and hence the displayed \(4X^6\log X\) factor.
Either version proves (3.1). For (3.2), divide by
\(\sqrt{x}\log^2(2x)\ge\sqrt2\log^24>0\); the right side tends to zero.
\(\square\)

---

## 4. The RH-equivalent corollary, and what it does not prove

The classical criterion is

\[
\mathrm{RH}
\iff
\psi(x)=x+O(\sqrt{x}\log^2x).
\tag{4.1}
\]

Combining (4.1) with (3.2) yields

\[
\boxed{
\mathrm{RH}
\iff
\sup_{X\ge X_0}
\sup_{2\le x\le X}
\frac{|\Psi_{K(X)}(x)-x|}
{\sqrt{x}\log^2(2x)}
<\infty.
}
\tag{4.2}
\]

This is an inherited equivalence: the approximation theorem transfers the
classical \(\psi\)-criterion to the permutation weights. It is not an
intrinsic Mighty-K property and it does not prove RH. In particular, (3.1)
proves only that \(\Psi_K\) approximates \(\psi\) uniformly; it does not prove
the bound on \(\Psi_K(x)-x\) itself.

---

## 5. Numerical check of the active-pair constant

The proof gives \(1/(5b)\). Exact prefix counts at bad-tier endpoints give much
larger minima:

| \(p\) | \(b=p^2+1\) | min active probability | \(1/(5b)\) | ratio to \(1/b\) |
|---:|---:|---:|---:|---:|
| 3 | 10 | 0.125585 | 0.020000 | 1.26 |
| 5 | 26 | 0.060355 | 0.007692 | 1.57 |
| 7 | 50 | 0.033943 | 0.004000 | 1.70 |
| 11 | 122 | 0.014842 | 0.001639 | 1.81 |
| 13 | 170 | 0.010828 | 0.001176 | 1.84 |
| 17 | 290 | 0.006480 | 0.000690 | 1.88 |
| 19 | 362 | 0.005227 | 0.000552 | 1.89 |

These are exact counts for the indicated prefixes, not Monte Carlo. They
support the sharper constant \(c/b\) with \(c\approx2\), but the proof above
uses the safe \(1/(5b)\).

---

## 6. Ledger

| Result | Status |
|---|---|
| Cross-tier active-pair probability \(\ge1/(5b)\) | Proved (Theorem 1) |
| All-primes Fourier decay (2.1) | Proved from Theorem 1 |
| Uniform approximation with \(K(X)=X^7\) | Proved (Theorem 3; sharper constant \(2X^6\log X\) available) |
| RH-equivalent \(\Psi_K\) criterion (4.2) | Follows from the classical \(\psi\)-criterion |
| Intrinsic Mighty-K RH equivalence | Open |
| RH proof | Open |

The constants in Theorems 2 and 3 are conservative. The log-coefficient step
now gives \(4X^3\delta_X\), so the final constant can be \(2X^6\log X\); the
theorem is stated with \(4\) for consistency with the conservative summation.
The true schedule threshold from the displayed exponents is \(X^{6+o(1)}\);
\(X^7\) is a safe explicit choice.
