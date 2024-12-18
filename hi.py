from fpdf import FPDF

# Initialize the PDF object
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.cell(200, 10, txt="Line Integral Solutions and Parameterization Explanation", ln=True, align='C')
pdf.ln(10)

# Content
conversation = """
Here are detailed steps for solving **problems 26, 27, 28, 29, and 30**.

---

## **Problem 26**

**Given:**

\[
\int_C (y - x) \, dx + x^2 y \, dy
\]
\[
C: y^2 = x^3 \text{ from } (1, -1) \text{ to } (1, 1).
\]

### **Steps:**
1. **Parameterize the curve \( C \):**
   From \( y^2 = x^3 \), let:
   - \( x = t^2 \) and \( y = t^3 \) for \( t \in [-1, 1] \).

   Then:
   - \( dx = \frac{d}{dt}(t^2) \, dt = 2t \, dt \),
   - \( dy = \frac{d}{dt}(t^3) \, dt = 3t^2 \, dt \).

2. **Substitute into the integral:**

   The integral becomes:
   \[
   \int_{-1}^1 \left[ (y - x) \, dx + x^2 y \, dy \right].
   \]

   Substitute \( x = t^2 \), \( y = t^3 \), \( dx = 2t \, dt \), \( dy = 3t^2 \, dt \):
   - \( y - x = t^3 - t^2 \),
   - \( x^2 y = (t^2)^2 (t^3) = t^7 \).

   Therefore:
   \[
   \int_{-1}^1 \left[ (t^3 - t^2)(2t) + t^7 (3t^2) \right] \, dt.
   \]

   Simplify each term:
   - \( (t^3 - t^2)(2t) = 2t^4 - 2t^3 \),
   - \( t^7 (3t^2) = 3t^9 \).

   Combine:
   \[
   \int_{-1}^1 \left( 2t^4 - 2t^3 + 3t^9 \right) \, dt.
   \]

3. **Integrate term by term:**

   - \( \int_{-1}^1 2t^4 \, dt = 2 \cdot \frac{2}{5} = \frac{4}{5} \) (even function),
   - \( \int_{-1}^1 -2t^3 \, dt = 0 \) (odd function),
   - \( \int_{-1}^1 3t^9 \, dt = 0 \) (odd function).

   Add results:
   \[
   \frac{4}{5} + 0 + 0 = \frac{4}{5}.
   \]

### Final Answer:
\[
\boxed{\frac{4}{5}}
\]

---

## **Problem 27**

**Given:**

\[
\int_C (x^2 + y^2) \, dx - x \, dy
\]
\[
C: x^2 + y^2 = 1, \text{ counterclockwise from } (1, 0) \text{ to } (0, 1).
\]

### **Steps:**

1. **Parameterize the curve \( C \):**
   Since \( x^2 + y^2 = 1 \) is a circle, parameterize it as:
   \[
   x = \cos t, \quad y = \sin t, \quad t \in [0, \frac{\pi}{2}].
   \]

   Then:
   - \( dx = -\sin t \, dt \),
   - \( dy = \cos t \, dt \).

2. **Substitute into the integral:**

   The integral becomes:
   \[
   \int_0^{\frac{\pi}{2}} \left[ (\cos^2 t + \sin^2 t)(-\sin t) - \cos t (\cos t) \right] \, dt.
   \]

   Simplify:
   - \( \cos^2 t + \sin^2 t = 1 \),
   - First term: \( (-\sin t) \),
   - Second term: \( -\cos^2 t \).

   Combine:
   \[
   \int_0^{\frac{\pi}{2}} \left[ -\sin t - \cos^2 t \right] \, dt.
   \]

3. **Integrate term by term:**

   - \( \int_0^{\frac{\pi}{2}} -\sin t \, dt = \cos t \Big|_0^{\frac{\pi}{2}} = 0 - 1 = -1 \),
   - \( \int_0^{\frac{\pi}{2}} -\cos^2 t \, dt = -\frac{\pi}{4} \) (using \( \int \cos^2 t \, dt = \frac{t}{2} + \frac{\sin(2t)}{4} \)).

   Combine:
   \[
   -1 - \frac{\pi}{4}.
   \]

### Final Answer:
\[
\boxed{-1 - \frac{\pi}{4}}
\]

---

## **Problem 28**

**Given:**

\[
\int_C (y - x) \, dx + xy \, dy
\]
\[
C: \text{ the line segment from } (3, 4) \text{ to } (2, 1).
\]

### **Steps:**

1. **Parameterize the line segment:**

   The line segment from \( (3, 4) \) to \( (2, 1) \) can be parameterized as:
   \[
   x = 3 - t, \quad y = 4 - 3t, \quad t \in [0, 1].
   \]

   Then:
   - \( dx = -dt \),
   - \( dy = -3 \, dt \).

2. **Substitute into the integral:**

   The integral becomes:
   \[
   \int_0^1 \left[ (y - x)(-1) + xy(-3) \right] \, dt.
   \]

   Substitute \( x = 3 - t \) and \( y = 4 - 3t \):
   - \( y - x = (4 - 3t) - (3 - t) = 1 - 2t \),
   - \( xy = (3 - t)(4 - 3t) = 12 - 9t - 4t + 3t^2 = 12 - 13t + 3t^2 \).

   Combine terms:
   \[
   \int_0^1 \left[ -(1 - 2t) - 3(12 - 13t + 3t^2) \right] \, dt.
   \]

   Simplify:
   \[
   \int_0^1 \left[ -1 + 2t - 36 + 39t - 9t^2 \right] \, dt.
   \]
   Combine like terms:
   \[
   \int_0^1 \left[ -37 + 41t - 9t^2 \right] \, dt.
   \]

3. **Integrate term by term:**

   - \( \int_0^1 -37 \, dt = -37 \),
   - \( \int_0^1 41t \, dt = 41 \cdot \frac{1}{2} = \frac{41}{2} \),
   - \( \int_0^1 -9t^2 \, dt = -9 \cdot \frac{1}{3} = -3 \).

   Combine:
   \[
   -37 + \frac{41}{2} - 3 = -40 + \frac{41}{2} = -\frac{80}{2} + \frac{41}{2} = -\frac{39}{2}.
   \]

### Final Answer:
\[
\boxed{-\frac{39}{2}}
\]

---

## **Problem 29**

**Given:**

\[
\int_C yz \, dx - xz \, dy + xy \, dz
\]
\[
C: x = e^t, \, y = e^{3t}, \, z = e^{-t}, \, t \in [0, 1].
\]

### **Steps:**

1. Compute \( dx, dy, dz \):
   - \( dx = e^t \, dt \),
   - \( dy = 3e^{3t} \, dt \),
   - \( dz = -e^{-t} \, dt \).

2. Substitute into the integral:
   \[
   \int_0^1 \left[ e^{3t} e^{-t} e^t - e^t e^{-t} (3e^{3t}) + e^t e^{3t} (-e^{-t}) \right] \, dt.
   \]

   Simplify and integrate.

---
Here are the detailed **steps for Problem 30**:

---

### **Problem 30**

**Given:**

\[
\int_C x^2 \, dx + xy \, dy + z^2 \, dz
\]
\[
C: x = \sin t, \, y = \cos t, \, z = t^2 \quad \text{where } t \in [0, \pi/2].
\]

---

### **Step 1: Compute \( dx \), \( dy \), and \( dz \):**

From the parameterizations:
- \( x = \sin t \), so \( dx = \cos t \, dt \),
- \( y = \cos t \), so \( dy = -\sin t \, dt \),
- \( z = t^2 \), so \( dz = 2t \, dt \).

---

### **Step 2: Substitute into the integral:**

The integral is:
\[
\int_C x^2 \, dx + xy \, dy + z^2 \, dz.
\]

Substitute \( x = \sin t \), \( y = \cos t \), \( dx = \cos t \, dt \), \( dy = -\sin t \, dt \), and \( dz = 2t \, dt \):
- \( x^2 = (\sin t)^2 \),
- \( xy = \sin t \cos t \),
- \( z^2 = (t^2)^2 = t^4 \).

The integral becomes:
\[
\int_0^{\pi/2} \left[ (\sin^2 t)(\cos t) + (\sin t \cos t)(-\sin t) + (t^4)(2t) \right] \, dt.
\]

Simplify each term:
- First term: \( (\sin^2 t)(\cos t) \),
- Second term: \( (\sin t \cos t)(-\sin t) = -\sin^2 t \cos t \),
- Third term: \( (t^4)(2t) = 2t^5 \).

Combine like terms:
\[
\int_0^{\pi/2} \left[ \sin^2 t \cos t - \sin^2 t \cos t + 2t^5 \right] \, dt.
\]

Notice that the first two terms cancel each other out:
\[
\int_0^{\pi/2} \left[ 0 + 2t^5 \right] \, dt.
\]

---

### **Step 3: Integrate the remaining term:**

The integral simplifies to:
\[
\int_0^{\pi/2} 2t^5 \, dt.
\]

Integrate \( t^5 \):
\[
\int t^5 \, dt = \frac{t^6}{6}.
\]

Thus:
\[
\int_0^{\pi/2} 2t^5 \, dt = 2 \cdot \frac{t^6}{6} \Big|_0^{\pi/2}.
\]

Evaluate at the limits:
- At \( t = \pi/2 \): \( \frac{(\pi/2)^6}{6} \),
- At \( t = 0 \): \( 0 \).

Therefore:
\[
2 \cdot \frac{(\pi/2)^6}{6} = \frac{2}{6} \cdot \left( \frac{\pi^6}{64} \right).
\]

Simplify:
\[
\frac{2}{6} = \frac{1}{3}, \quad \text{so:} \quad \frac{1}{3} \cdot \frac{\pi^6}{64} = \frac{\pi^6}{192}.
\]

---

### **Final Answer:**
\[
\boxed{\frac{\pi^6}{192}}
\]

To find the **values of \(x\), \(y\), and \(z\)** along a curve \(C\), follow the **parametric method**. Here's a detailed explanation:

---

### **1. What is Parameterization?**

A curve \( C \) can often be expressed in terms of a single variable \( t \) (the parameter). The coordinates \(x\), \(y\), and \(z\) are written as **functions of \(t\)**:

\[
x = f(t), \quad y = g(t), \quad z = h(t),
\]
where \( t \) lies within an interval \( [a, b] \).

---

### **2. Why Use Parameterization?**

Parameterization allows us to:
- Represent the motion or path of a curve,
- Simplify line integrals by substituting \(x\), \(y\), and \(z\) with explicit expressions involving \(t\).

---

### **3. How to Find \(x\), \(y\), and \(z\):**

To get \(x\), \(y\), and \(z\) values:
1. **Identify the curve**: The curve \(C\) is usually given in some form, such as:
   - Explicit equations: e.g., \(y^2 = x^3\),
   - Parametric form: \(x = f(t), y = g(t)\),
   - Geometric description: e.g., a line segment or circle.

2. **Introduce a parameter \(t\)**: 
   - If the curve is explicitly given, introduce \(t\) to describe \(x\), \(y\), and \(z\) as functions.
   - If the curve is a straight line or a simple path, parameterize the line segment between two points.

3. **Express the coordinates**: Write \(x\), \(y\), and \(z\) as functions of \(t\).

4. **Find derivatives**: Compute \(dx\), \(dy\), and \(dz\) by differentiating \(x\), \(y\), and \(z\) with respect to \(t\).

---

### **4. Examples of Parameterization**

Let's look at **different curve types** to see how to find \(x\), \(y\), and \(z\).

---

#### **Example 1: A Line Segment**

A line segment connecting two points \(P_1 = (x_1, y_1, z_1)\) and \(P_2 = (x_2, y_2, z_2)\) can be parameterized as:

\[
x = x_1 + t(x_2 - x_1), \quad y = y_1 + t(y_2 - y_1), \quad z = z_1 + t(z_2 - z_1),
\]
where \( t \in [0, 1] \).

**Example:** Find \(x, y, z\) for the line segment from \( (3, 4, 0) \) to \( (2, 1, 5) \).

- \( x_1 = 3, y_1 = 4, z_1 = 0 \),
- \( x_2 = 2, y_2 = 1, z_2 = 5 \).

The parameterization is:
\[
x = 3 + t(2 - 3) = 3 - t, \quad y = 4 + t(1 - 4) = 4 - 3t, \quad z = 0 + t(5 - 0) = 5t.
\]

---

#### **Example 2: A Circle**

A circle of radius \(r\) centered at \((0, 0)\) can be parameterized as:
\[
x = r \cos t, \quad y = r \sin t, \quad t \in [0, 2\pi].
\]

**Example:** Find \(x\) and \(y\) for a unit circle (\(r = 1\)).

\[
x = \cos t, \quad y = \sin t, \quad t \in [0, 2\pi].
\]

---

#### **Example 3: A Curve Given Implicitly**

If the curve is given implicitly, e.g., \(y^2 = x^3\), you need to:

1. Express one variable in terms of \(t\) (e.g., let \(x = t\)),
2. Find the corresponding \(y\)-value.

**Example:** For \(y^2 = x^3\), let \(x = t^2\) (positive values only). Then:
\[
y = t^3.
\]

The parameterization is:
\[
x = t^2, \quad y = t^3.
\]

---

#### **Example 4: A Helix**

A 3D helix can be described as:
\[
x = r \cos t, \quad y = r \sin t, \quad z = ct,
\]
where \(r\) is the radius, \(c\) is the vertical growth rate, and \(t\) is the parameter.

**Example:** For \(r = 1\) and \(c = 2\), the helix is:
\[
x = \cos t, \quad y = \sin t, \quad z = 2t, \quad t \in [0, 2\pi].
\]

---

### **5. General Steps for Substitution in Integrals**

Once you find \(x\), \(y\), \(z\), and their derivatives \(dx\), \(dy\), and \(dz\):
1. Substitute \(x = f(t)\), \(y = g(t)\), \(z = h(t)\),
2. Substitute \(dx = f'(t) dt\), \(dy = g'(t) dt\), \(dz = h'(t) dt\),
3. Replace the limits of integration with the corresponding \(t\)-values.

---

### **Conclusion**

To summarize:
1. Identify the curve and type of description (line, circle, implicit, or 3D path),
2. Introduce a parameter \(t\),
3. Write \(x\), \(y\), and \(z\) as functions of \(t\),
4. Differentiate \(x\), \(y\), \(z\) to find \(dx\), \(dy\), \(dz\),
5. Use these values to simplify the integral.

Would you like me to solve another specific example or clarify a step further? 😊
"""

# Add the conversation text
for line in conversation.split("\n"):
    pdf.multi_cell(0, 8, txt=line)
    pdf.ln(1)

# Save the PDF
pdf_output_path = "C:\Musfique's Folder\Python\Shongjog-Python-Course\Chapter_15.2_Line_Integral_Evaluation.pdf"
pdf.output(pdf_output_path)

pdf_output_path
