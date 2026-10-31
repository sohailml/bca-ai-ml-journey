# 🌐 Web Programming - Unit 3: Tables and Text Styling in HTML

> **Course:** BCA - Semester 1  
> **Topic:** HTML Tables, Attributes, Text Styling (CSS), Lists & Semantic Tags

---

## 📑 Table of Contents
1. [Introduction & Objectives](#-1-introduction--objectives)
2. [HTML Tables (Complete Guide)](#-2-html-tables-complete-guide)
   - [Basic Structure & Tags](#21-basic-structure--tags)
   - [Table Attributes (Border, Cellpadding, Cellspacing)](#22-table-attributes)
   - [Rowspan & Colspan (Exam Important)](#23-rowspan--colspan-exam-important)
   - [Styling Tables with CSS](#24-styling-tables-with-css)
3. [Text Styling & Fonts in HTML](#-3-text-styling--fonts-in-html)
   - [Deprecated HTML Tags/Attributes](#31-deprecated-html-tagsattributes)
   - [Modern CSS Text Styling (Exam Important)](#32-modern-css-text-styling-exam-important)
4. [HTML Lists (Complete Guide)](#-4-html-lists-complete-guide)
   - [Unordered List (`<ul>`)](#41-unordered-list-ul)
   - [Ordered List (`<ol>`)](#42-ordered-list-ol)
   - [Definition List (`<dl>`)](#43-definition-list-dl)
   - [Nested Lists (Exam Important)](#44-nested-lists-exam-important)
5. [Summary, Cheat Sheet & Q&A](#-5-summary-cheat-sheet--qa)

---

## 📌 1. Introduction & Objectives

Web development mein **Tables** aur **Text Styling** do fundamental tools hain. Tables data ko rows aur columns mein structured tarike se present karte hain, jabki Text Styling (CSS) se hum text ko visually appealing banate hain (font, size, color, alignment, etc.).

**Objectives:**
*   Table construction ke essential attributes (border, headers, rows, cells) identify karna.
*   Well-structured tables banane ke principles samajhna.
*   CSS styles (border, cell spacing, cell padding) implement karna.
*   Font selection, size, color, alignment ka user engagement par impact analyze karna.
*   Advanced text styling techniques aur responsive web pages develop karna.

---

## 🗂️ 2. HTML Tables (Complete Guide)

HTML Table ek structured grid hota hai jisme data rows aur columns mein organize hota hai.

### 2.1 Basic Structure & Tags

Ek HTML table in elements se milkar banta hai:

| Tag | Description (Kya Karta Hai?) |
| :--- | :--- |
| **`<table>`** | Table ka container element. |
| **`<tr>`** | Table Row (ek row define karta hai). |
| **`<th>`** | Table Header cell (bold aur centered by default). |
| **`<td>`** | Table Data cell (normal data store karta hai). |
| **`<caption>`** | Table ka title/caption (table ke upar dikhta hai). |
| **`<thead>`** | Header section ko group karta hai. |
| **`<tbody>`** | Body section (data rows) ko group karta hai. |
| **`<tfoot>`** | Footer section (summary) ko group karta hai. |
| **`<colgroup>`** | Columns ke group ko specify karta hai formatting ke liye. |
| **`<col>`** | Individual column ki properties define karta hai. |

**Basic Syntax Example:**
```html
<table border="1">
  <caption>Student Data</caption>
  <thead>
    <tr>
      <th>Name</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Rahul</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Aman</td>
      <td>21</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Total</td>
      <td>2</td>
    </tr>
  </tfoot>
</table>
```

> [!NOTE]
> `<thead>`, `<tbody>`, `<tfoot>` optional hain, par inka use structure aur accessibility ke liye accha hota hai.

### 2.2 Table Attributes

*   **`border="1"`**: Table ke around 1-pixel ka border lagata hai.
*   **`cellpadding="10"`**: Cell ke content aur border ke beech space (padding) add karta hai.
*   **`cellspacing="0"`**: Do cells ke beech ka gap (spacing) define karta hai.

**Example:**
```html
<table border="1" cellpadding="10" cellspacing="0">
  <!-- table content -->
</table>
```

> [!WARNING]
> **Deprecated Alert:** HTML5 mein table styling ke liye `border`, `cellpadding`, `cellspacing` attributes ko **deprecated** kar diya gaya hai. Aaj kal inki jagah **CSS** use kiya jata hai.

### 2.3 Rowspan & Colspan (Exam Important)

PDF mein inka zikr chhota sa hai, par exams mein ye bahut important hain.

*   **`colspan`**: Ek cell ko multiple columns mein span (merge) karne ke liye.
*   **`rowspan`**: Ek cell ko multiple rows mein span (merge) karne ke liye.

**Example (Colspan):**
```html
<table border="1">
  <tr>
    <th colspan="2">Student Details</th>
  </tr>
  <tr>
    <td>Name</td>
    <td>Rahul</td>
  </tr>
</table>
```

**Example (Rowspan):**
```html
<table border="1">
  <tr>
    <th rowspan="2">Name</th>
    <td>Rahul</td>
  </tr>
  <tr>
    <td>Aman</td>
  </tr>
</table>
```

### 2.4 Styling Tables with CSS

Aaj kal tables ko style karne ke liye CSS (Inline, Internal, ya External) use karte hain.

**Important CSS Properties for Tables:**
*   **`border-collapse: collapse;`**: Adjacent cells ke borders ko ek single line mein merge kar deta hai.
*   **`width: 100%;`**: Table ko container ki full width de deta hai.
*   **`text-align: center;`**: Table ke andar text ko center align karta hai.
*   **`background-color`**: Row ya cell ka background color set karta hai (striped effect ke liye).

**Example (Inline CSS):**
```html
<table border="1" style="border-collapse: collapse; width: 100%; text-align: center;">
  <tr style="background-color: #333; color: #fff; font-weight: bold;">
    <th>Header 1</th>
    <th>Header 2</th>
  </tr>
  <tr style="background-color: #f2f2f2;">
    <td>Data 1</td>
    <td>Data 2</td>
  </tr>
  <tr style="background-color: #fff;">
    <td>Data 3</td>
    <td>Data 4</td>
  </tr>
</table>
```

---

## 🎨 3. Text Styling & Fonts in HTML

### 3.1 Deprecated HTML Tags/Attributes

Pehle HTML mein text styling ke liye direct tags use hote the, par aajkal ye **deprecated** hain (HTML5 mein supported nahi hain).

*   **`<font>` tag:** Text ka size, color, face set karne ke liye.
*   **`size` attribute:** `<h1>`, `<p>` par direct size dene ke liye (e.g., `size="6"`).
*   **`face`, `color` attributes:** Font family aur text color set karne ke liye.

**Deprecated Example (Mat use karo):**
```html
<p face="Arial" color="blue" size="3">This is deprecated styling.</p>
<font size="2" color="red">Old way of styling.</font>
```

### 3.2 Modern CSS Text Styling (Exam Important)

Aaj kal text styling ke liye CSS use hoti hai. Ye properties exam mein bahut aati hain:

| CSS Property | Description (Kya Karti Hai?) | Example Values |
| :--- | :--- | :--- |
| **`color`** | Text ka color set karta hai. | `red`, `#333`, `rgb(0,0,0)` |
| **`font-family`** | Font ka type set karta hai. | `Arial`, `Times New Roman`, `sans-serif` |
| **`font-size`** | Text ka size set karta hai. | `16px`, `1.2em`, `large` |
| **`font-weight`** | Text ko bold ya normal banata hai. | `bold`, `normal`, `900` |
| **`font-style`** | Text ko italic banata hai. | `italic`, `normal` |
| **`text-align`** | Text ka alignment set karta hai. | `left`, `center`, `right`, `justify` |
| **`text-decoration`** | Underline, overline, line-through lagata hai. | `underline`, `none`, `line-through` |
| **`text-transform`** | Text ka case change karta hai. | `uppercase`, `lowercase`, `capitalize` |
| **`line-height`** | Lines ke beech ka space set karta hai. | `1.5`, `20px` |
| **`letter-spacing`** | Characters ke beech ka space set karta hai. | `2px`, `0.1em` |
| **`text-shadow`** | Text ko shadow effect deta hai. | `2px 2px 4px #000` |

**Example:**
```html
<style>
  h1 {
    color: #2c3e50;
    font-family: Arial, sans-serif;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 2px;
    text-shadow: 2px 2px 4px #ccc;
  }
  p {
    font-size: 16px;
    line-height: 1.6;
    text-align: justify;
  }
</style>
```

---

## 📋 4. HTML Lists (Complete Guide)

Lists web page par information ko structured, ordered ya unordered format mein present karne ka tarika hai. 3 main types hain:

### 4.1 Unordered List (`<ul>`)
*   Items bullet points ke saath dikhte hain.
*   Har item `<li>` (list item) tag ke andar hota hai.

**Example:**
```html
<ul>
  <li>Apples</li>
  <li>Oranges</li>
  <li>Bananas</li>
</ul>
```

### 4.2 Ordered List (`<ol>`)
*   Items sequential numbers ya letters ke saath dikhte hain.
*   Har item `<li>` tag ke andar hota hai.

**Example:**
```html
<ol>
  <li>First</li>
  <li>Second</li>
  <li>Third</li>
</ol>
```

**Attributes (Exam Important):**
*   **`type`**: Numbering style change karta hai.
    *   `type="1"`: 1, 2, 3 (default)
    *   `type="A"`: A, B, C
    *   `type="a"`: a, b, c
    *   `type="I"`: I, II, III (Roman)
    *   `type="i"`: i, ii, iii
*   **`start`**: Starting number set karta hai (e.g., `start="5"`).
*   **`reversed`**: Counting order ulta kar deta hai (e.g., 3, 2, 1).

**Example:**
```html
<ol type="I" start="5">
  <li>Item 5</li>
  <li>Item 6</li>
</ol>
```

### 4.3 Definition List (`<dl>`)
*   Terms aur unki definitions ko pair karke dikhata hai.
*   `<dt>` (Definition Term): Term ka naam.
*   `<dd>` (Definition Description): Term ki definition.

**Example:**
```html
<dl>
  <dt>HTML</dt>
  <dd>Hypertext Markup Language</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets</dd>
</dl>
```

### 4.4 Nested Lists (Exam Important)
Aap ek list ke andar dusri list bana sakte hain (jaise menu ya outline).

**Example:**
```html
<ul>
  <li>Fruits
    <ul>
      <li>Apple</li>
      <li>Banana</li>
    </ul>
  </li>
  <li>Vegetables
    <ul>
      <li>Carrot</li>
      <li>Potato</li>
    </ul>
  </li>
</ul>
```

---

## 📝 5. Summary, Cheat Sheet & Q&A

### 5.1 Summary
*   **Tables:** Data ko rows/columns mein dikhane ke liye (`<table>`, `<tr>`, `<th>`, `<td>`).
*   **Table Attributes:** `border`, `cellpadding`, `cellspacing` (deprecated in HTML5, use CSS).
*   **Rowspan/Colspan:** Cells ko merge karne ke liye.
*   **CSS Table Styling:** `border-collapse`, `width`, `text-align`, `background-color`.
*   **Text Styling:** `<font>` tag deprecated hai. CSS properties (`color`, `font-size`, `text-align`, etc.) use karo.
*   **Lists:** 
    *   `<ul>` (unordered, bullets)
    *   `<ol>` (ordered, numbers/letters)
    *   `<dl>` (definition, terms and descriptions)
*   **List Attributes:** `type`, `start`, `reversed` (for `<ol>`).
*   **Nesting:** Lists ke andar lists bana sakte hain.

### 5.2 Cheat Sheet (Quick Revision)

```html
<!-- TABLE -->
<table border="1" style="border-collapse: collapse;">
  <caption>Title</caption>
  <thead>
    <tr><th>Header</th></tr>
  </thead>
  <tbody>
    <tr><td>Data</td></tr>
  </tbody>
</table>

<!-- LISTS -->
<ul>
  <li>Unordered Item</li>
</ul>

<ol type="A" start="3" reversed>
  <li>Ordered Item</li>
</ol>

<dl>
  <dt>Term</dt>
  <dd>Definition</dd>
</dl>
```

### 5.3 Self-Assessment Questions (PDF Answers)
1.  **What HTML element defines a table?** `<table>`
2.  **What HTML element is used for header cells?** `<th>`
3.  **How can you make table borders collapse into a single line?** CSS property `border-collapse: collapse;`
4.  **What attribute specifies the space between table cells?** `cellspacing`
5.  **What HTML element defines a table row?** `<tr>`
6.  **What HTML element creates an unordered list?** `<ul>`
7.  **What tag represents a list item in HTML?** `<li>`
8.  **What attribute in an ordered list changes the numbering style to Roman numerals?** `type="I"` (or `type="i"`)
9.  **Which HTML element is used to define a description list?** `<dl>`
10. **What tag defines a term in a definition list?** `<dt>`

### 5.4 Terminal Questions (Hints for Long Answers)
1.  **Structure of HTML Table:** `<table>` container, `<caption>`, `<thead>` (headers), `<tbody>` (data), `<tfoot>` (footer). Use case: Tabular data display (e.g., student marks, product list).
2.  **Key Attributes of Table:** `border`, `cellpadding`, `cellspacing` (deprecated, use CSS), `colspan`, `rowspan`. These control appearance and behavior (spacing, merging).
3.  **Accessibility in Tables:** Use `<caption>` for title, `<th>` with `scope` attribute (e.g., `scope="col"`), avoid tables for layout (use CSS).
4.  **Compare Lists:** `<ul>` (bullets, order not important), `<ol>` (numbers, order important), `<dl>` (terms/definitions, like dictionary). Examples: Menu (`<ul>`), Steps (`<ol>`), Glossary (`<dl>`).
5.  **List Nesting:** Putting a list inside an `<li>` of another list. Use case: Multi-level menus, outlines.
6.  **Semantic Markup & SEO:** Using semantic tags (`<ul>`, `<ol>`, `<table>`) helps search engines and screen readers understand the content structure, improving SEO and accessibility.

### 5.5 Extra Practice Questions (Exam Special)
1.  What is the difference between `colspan` and `rowspan`?
2.  Write the HTML code to create a table with 3 columns and 2 rows.
3.  How do you change the background color of a table row using CSS?
4.  What is the difference between `<ul>` and `<ol>`?
5.  Write the code to create a nested list (e.g., fruits inside a grocery list).
6.  Why is the `<font>` tag deprecated in HTML5?

---
> **💡 Bhai ka Gyan:** Exam mein Table structure (`<thead>`, `<tbody>`), `rowspan`/`colspan`, aur List types (`<ul>`, `<ol>`, `<dl>`) ke questions pakke aate hain. `border-collapse` aur `cellpadding`/`cellspacing` ka difference zarur yaad rakhna. Aur haan, `<font>` tag deprecated hai, ye question bhi aata hai! All the best! 🚀
