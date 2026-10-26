# 🌐 Web Programming - Unit 2: Advanced HTML Features

> **Course:** BCA - Semester 1  
> **Topic:** Advanced HTML (Text, Images, Links, Backgrounds)

---

## 📑 Table of Contents
1. [Introduction to HTML5](#-1-introduction-to-html5)
2. [Inserting Texts (Text kaise daalein)](#-2-inserting-texts-text-kaise-daalein)
3. [Text Alignment (Deprecated)](#-3-text-alignment-deprecated)
4. [Using Images in Pages](#-4-using-images-in-pages)
5. [Hyperlinks (Text & Images)](#-5-hyperlinks-text--images)
6. [Bookmarks (Page Navigation)](#-6-bookmarks-page-navigation)
7. [Background & Color Controls](#-7-background--color-controls)
8. [Summary & Q&A](#-8-summary--qa)

---

## 🚀 1. Introduction to HTML5

HTML5 latest aur sabse advanced version hai. Isme developers aur users dono ke liye naye features aaye hain. Ye W3C aur WHATWG ke collaboration se bana hai.

**HTML5 ke 7 Main Features:**
1.  **Multimedia Integration:** Bina kisi third-party plugin (jaise Flash) ke direct `<video>` aur `<audio>` embed kar sakte hain.
2.  **Canvas for Graphics:** `<canvas>` tag se 2D graphics aur visualizations banaye ja sakte hain (JavaScript ke saath).
3.  **Enhanced Forms:** Date pickers, email validation, range sliders jaise naye form elements aaye.
4.  **Offline Capabilities:** Internet ke bina bhi website ke kuch hisse access kiye ja sakte hain (offline caching).
5.  **Improved Interactivity:** Bina zyada JavaScript code likhe interactive elements banana aasan hua.
6.  **Semantic Elements:** `<header>`, `<footer>`, `<section>` jaise tags aaye jo SEO aur accessibility ke liye acche hain.
7.  **WebSockets:** Real-time bidirectional communication (jaise live chat) possible hui.

**HTML5 ke Benefits:**
*   **Cross-Browser Compatibility:** Sabhi modern browsers (IE included) HTML5 ko support karte hain.
*   **Better User Experience:** Dynamic websites banana aasan hua.
*   **Video/Audio Support:** Bina plugin ke multimedia support.

---

## 📝 2. Inserting Texts (Text kaise daalein)

Web page par text dikhane ke liye alag-alag tags hote hain. Yahan sabse important tags ki list hai, syntax aur examples ke saath:

### 2.1 Paragraphs (`<p>`)
Text ko paragraph format mein likhne ke liye.
*   **Syntax:** `<p>Your text goes here.</p>`
*   **Example:**
    ```html
    <p>This is a paragraph of text.</p>
    ```
*   *Note:* Browser automatically iske upar aur niche thodi space chhod deta hai (jaise book ke paragraphs).

### 2.2 Headings (`<h1>` to `<h6>`)
Page par headings aur subheadings ke liye. `<h1>` sabse bada aur important hota hai, `<h6>` sabse chhota.
*   **Syntax:** `<h1>Your heading</h1>`
*   **Example:**
    ```html
    <h1>This is the biggest one</h1>
    <h2>This one is a little smaller</h2>
    <h3>This one is even smaller</h3>
    <h4>They keep getting smaller</h4>
    <h5>This one isn't even that big</h5>
    <h6>Pretty small now, actually</h6>
    ```

### 2.3 Line Breaks (`<br>`)
Line break dene ke liye. Ye ek **empty element** hai (iska closing tag nahi hota).
*   **Syntax:** `<br>`
*   **Example:**
    ```html
    This is some text. <br>Here's a new line of text.
    ```

### 2.4 Preformatted Text (`<pre>`)
Jo text tu HTML code mein jaisa likhega (spaces, line breaks), `<pre>` tag usko exactly waisa hi dikhayega.
*   **Syntax:** `<pre>Your preformatted text</pre>`
*   **Example:**
    ```html
    <pre>
        This is preformatted text.
    </pre>
    ```

### 2.5 Blockquotes (`<blockquote>`)
Kisi ka quote ya citation dikhane ke liye.
*   **Syntax:** `<blockquote>Your quoted text</blockquote>`
*   **Example:**
    ```html
    <blockquote>
        To be or not to be, that is the question.
        - Shakespeare
    </blockquote>
    ```

### 2.6 Lists (`<ol>` and `<ul>`)
*   **Ordered List (`<ol>`):** Numbered list (1, 2, 3).
    ```html
    <ol>
        <li>First item</li>
        <li>Second item</li>
    </ol>
    ```
*   **Unordered List (`<ul>`):** Bullet points (dots).
    ```html
    <ul>
        <li>Apples</li>
        <li>Bananas</li>
    </ul>
    ```

### 2.7 Anchors (`<a>` for Hyperlinks)
Hyperlinks banane ke liye.
*   **Syntax:** `<a href="URL">Link Text</a>`
*   **Example:**
    ```html
    <a href="https://www.example.com">Visit Example.com</a>
    ```

### 2.8 Comments (`<!-- -->`)
Comments web page par visible nahi hote, sirf code mein notes likhne ke liye use hote hain.
*   **Syntax:** `<!-- Your comment here -->`
*   **Example:** `<!-- This is a comment -->`

### 2.9 Text Formatting (`<em>`, `<strong>`, `<u>`, `<s>`)
Text ko format karne ke liye:
*   `<em>`: Italic (emphasis)
*   `<strong>`: Bold (strong importance)
*   `<u>`: Underline
*   `<s>`: Strikethrough
*   **Example:**
    ```html
    <p><em>This is italic text</em></p>
    <p><strong>This is bold text</strong></p>
    <p><u>This is underlined text</u></p>
    <p><s>This is strikethrough text</s></p>
    ```

---

## 📐 3. Text Alignment (Deprecated)

Pehle HTML mein text align karne ke liye `align` attribute use hota tha (jaise `<p>`, `<h1>`, `<div>`, `<td>` ke andar).

**Align Attribute ki Values:**
*   `left`: Text left mein align.
*   `center`: Text horizontally center mein.
*   `right`: Text right mein align.
*   `justify`: Text left aur right dono edges ko touch karega.

**Examples:**
```html
<!-- Left Alignment -->
<p align="left">This is left-aligned text.</p>

<!-- Center Alignment -->
<h1 align="center">This is centered text.</h1>

<!-- Right Alignment -->
<div align="right">This is right-aligned text.</div>

<!-- Justified Text -->
<p align="justify">This is justified text. It will spread evenly between the left and right edges.</p>
```

> [!WARNING]
> **Deprecated:** HTML5 mein `align` attribute **deprecated** (purana) ho chuka hai. Aaj kal text align karne ke liye **CSS** (jaise `style="text-align: center;"`) ka use kiya jata hai, taaki design aur code alag rahein aur modern standards follow hon.

---

## 🖼️ 4. Using Images in Pages

Web page par images lagane ke liye `<img>` tag use hota hai. Ye bhi ek **empty (self-closing)** tag hai.

### 4.1 `<img>` Tag Attributes:
*   `src` (Required): Image ka source URL ya file path.
*   `alt` (Required): Alternative text. Agar image load na ho, toh ye text dikhta hai. (Accessibility ke liye bahut zaroori hai).
*   `width` (Optional): Image ki width pixels mein.
*   `height` (Optional): Image ki height pixels mein.

**Basic Image Insertion:**
```html
<img src="example.jpg" alt="An example image">
```

**Image with Specified Dimensions:**
```html
<img src="example.jpg" alt="An example image" width="300" height="200">
```

**Relative Image Paths (Agar image same folder ya subfolder mein ho):**
```html
<img src="images/example.jpg" alt="An example image">
```

**Image Links (Image ko clickable banana):**
```html
<a href="https://example.com">
    <img src="example.jpg" alt="Link to Example.com">
</a>
```

**Responsive Images (Screen size ke hisaab se adjust karna):**
```html
<style>
    img {
        max-width: 100%;
        height: auto;
    }
</style>
```
*(Note: HTML formats jaise JPEG, PNG, GIF, SVG support karta hai. Alt text hamesha meaningful rakho).*

> [!NOTE]
> Jab browser image load karta hai, toh wo image ko web server se mangata hai. Agar image apni jagah se hat gayi, toh "broken link icon" aur `alt` text dikhega.

---

## 🔗 5. Hyperlinks (Text & Images)

Hyperlinks ka matlab hai ek page se dusre page par navigate karna. Iske liye `<a>` (anchor) tag use hota hai.

### 5.1 Text Hyperlink
```html
<a href="https://www.example.com">Visit Example.com</a>
```
*   `href`: Destination URL.
*   `Link Text`: Jo clickable text dikhega.

### 5.2 Image Hyperlink
```html
<a href="https://www.example.com">
    <img src="image.jpg" alt="An example image">
</a>
```

### 5.3 Target Attribute (`target="_blank"`)
Agar tu chahta hai ki link naye tab mein khule, toh `target="_blank"` use kar.
```html
<a href="https://www.example.com" target="_blank">Visit Example.com</a>
```
*(Note: `alt` text image links ke liye bahut important hai taaki screen readers samajh sakein ki link kahan jayega).*

---

## 📌 6. Bookmarks (Page Navigation)

Bookmarks ka use long web page ke andar specific section par jump karne ke liye hota hai (jaise Table of Contents). Ise **Anchor Bookmarks** ya **Named Anchors** bhi kehte hain.

### 6.1 `name` Attribute se Bookmark (Purana Tarika)
Pehle `<a>` tag ke andar `name` attribute use hota tha.

**Example:**
```html
<h1>Table of Contents</h1>
<ul>
    <li><a href="#section1">Section 1</a></li>
    <li><a href="#section2">Section 2</a></li>
    <li><a href="#section3">Section 3</a></li>
</ul>

<h2><a name="section1"></a>Section 1</h2>
<p>This is the content of Section 1.</p>

<h2><a name="section2"></a>Section 2</h2>
<p>This is the content of Section 2.</p>

<h2><a name="section3"></a>Section 3</h2>
<p>This is the content of Section 3.</p>
```

### 6.2 `id` Attribute se Bookmark (Modern Way)
Aaj kal kisi bhi element (jaise heading ya div) par `id` attribute de kar bookmark banaya jata hai.

**Example:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML Bookmarks Example</title>
</head>
<body>
    <h1>Table of Contents</h1>
    <ul>
        <li><a href="#section1">Section 1</a></li>
        <li><a href="#section2">Section 2</a></li>
        <li><a href="#section3">Section 3</a></li>
    </ul>

    <h2 id="section1">Section 1</h2>
    <p>This is the content of Section 1.</p>

    <h2 id="section2">Section 2</h2>
    <p>This is the content of Section 2.</p>

    <h2 id="section3">Section 3</h2>
    <p>This is the content of Section 3.</p>
</body>
</html>
```
*(Jab user "Section 1" par click karega, browser automatically us heading par scroll ho jayega).*

---

## 🎨 7. Background & Color Controls

Web page ka background set karna design ka important part hai. HTML5 mein background set karne ke liye **CSS** ka use kiya jata hai.

### 7.1 Background with Color
`<body>` tag ke andar `style` attribute aur CSS ki `background-color` property use karte hain.

**Example (Color Name):**
```html
<!DOCTYPE html>
<html>
<body style="background-color: aquamarine;">
    <h1>HTML Articles</h1>
</body>
</html>
```
*   Hum color ko override bhi kar sakte hain (jaise `khaki`).

**Example (RGB Value):**
RGB value red, green, blue ki intensity batati hai (0 to 255, ya hex 00 to FF).
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            background-color: rgb(20, 30, 1);
        }
    </style>
</head>
<body>
    <h1>HTML Articles</h1>
</body>
</html>
```

### 7.2 Background with Image
Background mein image lagane ke liye CSS use karte hain.

**Example (Table background):**
```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML Background Images</title>
</head>
<body>
    <!-- Set table background -->
    <table background="/images/html.gif" width="100%" height="100">
        <tr><td>
            This background is filled up with HTML image.
        </td></tr>
    </table>
</body>
</html>
```

### 7.3 Patterned and Transparent Background
Website ko fast load karne ke liye chhoti se chhoti image (jaise 1x1 pixel) ka use karein jo repeat ho jaye. Isse transparency aur design dono handle ho jate hain bina page ka size badhaye.

**Example:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML Background Images</title>
</head>
<body>
    <!-- Set a table background using pattern -->
    <table background="/images/pattern1.gif" width="100%" height="100">
        <tr>
            <td>
                This background is filled up with a pattern image.
            </td>
        </tr>
    </table>
    
    <!-- Another example on table background using pattern -->
    <table background="/images/pattern2.gif" width="100%" height="100">
        <tr>
            <td>
                This background is filled up with a pattern image.
            </td>
        </tr>
    </table>
</body>
</html>
```

> [!WARNING]
> **Deprecated:** HTML5 mein `<body bgcolor="...">` ya `<body background="...">` attributes **deprecated** ho chuke hain. Inki jagah CSS (`background-color` aur `background-image`) ka use karna chahiye.

---

## 📝 8. Summary & Q&A

### Summary
Is chapter mein humne HTML ke advanced features seekhe:
*   **Text Insertion:** `<p>`, headings, lists, formatting tags.
*   **Text Alignment:** `align` attribute (deprecated).
*   **Images:** `<img>` tag, `src`, `alt`, dimensions, links.
*   **Hyperlinks:** Text aur image links, `target` attribute.
*   **Bookmarks:** `name` aur `id` attributes se page navigation.
*   **Background:** CSS `background-color`, `background-image` (modern tarika).

### Quick Revision (Self-Assessment & Terminal Questions)

**Q1. What HTML element is used to define paragraphs of text?**
*   *Ans:* `<p>`

**Q2. Which HTML element is used to create hyperlinks?**
*   *Ans:* `<a>` (anchor tag)

**Q3. Which HTML attribute was historically used for text alignment but is now deprecated?**
*   *Ans:* `align` attribute (modern approach is CSS).

**Q4. In HTML, what value would you use with the align attribute to center text horizontally?**
*   *Ans:* `center`

**Q5. Which HTML element is used to display images on a web page?**
*   *Ans:* `<img>`

**Q6. What attribute in the `<img>` element specifies the image file's source (URL)?**
*   *Ans:* `src`

**Q7. What HTML attribute is used to create bookmarks within a web page using the `<a>` element?**
*   *Ans:* `name` attribute (older way) or `id` (modern way).

**Q8. What CSS property is used to set the background color of an HTML element?**
*   *Ans:* `background-color`

**Q9. Which HTML attribute for setting background properties is deprecated in HTML5?**
*   *Ans:* `bgcolor` (and `background` attribute in `<body>`).

**Q10. Explain the difference between `<em>` and `<strong>` elements?**
*   *Ans:* `<em>` text ko italic karta hai (emphasis), aur `<strong>` text ko bold karta hai (strong importance).

**Q11. Why is it important to provide meaningful `alt` text for images?**
*   *Ans:* Agar image load na ho toh text dikhata hai, aur visually impaired users (screen readers) ke liye page ko accessible banata hai.

**Q12. Explain the difference between `name` and `id` attribute for bookmarks?**
*   *Ans:* `name` attribute purane HTML mein use hota tha `<a>` tag ke andar. `id` attribute modern HTML5 mein kisi bhi element par use ho sakta hai aur ye zyada flexible hai.

---
> **💡 Bhai ka Gyan:** Exam mein `<img>` tag ke attributes (`src`, `alt`), Bookmarks (`id` vs `name`), aur deprecated attributes (jaise `align`, `bgcolor`) ka difference zarur pucha jata hai. Code likhne ki practice zarur karna, especially image links aur bookmarks wala part!
