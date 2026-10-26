# 🌐 Web Programming - Unit 1: Introduction to HTML

> **Course:** BCA - Semester 1  
> **Topic:** Introduction to HTML & Web Programming  
---

## 📑 Table of Contents
1. [Introduction (WWW vs Internet)](#-1-introduction-www-vs-internet)
2. [Definitions (Web Programming & HTML)](#-2-definitions-web-programming--html)
3. [Features of Web Programming](#-3-features-of-web-programming)
4. [Uses of HTML](#-4-uses-of-html)
5. [Versions of HTML](#-5-versions-of-html)
6. [HTML Syntax & First Web Page](#-6-html-syntax--first-web-page)
7. [Head and Body Sections of HTML](#-7-head-and-body-sections-of-html)
8. [Quick Revision (Q&A)](#-8-quick-revision-qa)

---

## 🌍 1. Introduction (WWW vs Internet)

**WWW (World Wide Web) kya hai?** 
Ye ek information realm hai jahan documents aur web resources **URIs** (Uniform Resource Identifiers) se identify hote hain. Ye aapas mein **hypertext links** se jude hote hain aur internet ke through access hote hain. Web pages mainly **HTML** (Hypertext Markup Language) mein bante hain. Ek website alag-alag web pages ka collection hoti hai.

**Internet kya hai?** 
Internet computers ka ek bada network hai jo **TCP/IP** (Transmission Control Protocol/Internet Protocol) ke through connect hota hai. Ye 1982 mein establish hua tha aur program-to-program communication enable karta hai. (Internet hardware/network hai, WWW usme chalne wali service hai).

---

## 📖 2. Definitions (Web Programming & HTML)

*   **Web Programming:** Ye interactive aur dynamic websites banane ka art aur science hai. Isme frontend (UI) aur backend (server, database, authentication) dono aate hain. Iske liye HTML, CSS, JavaScript, Python, PHP etc. languages use hoti hain.
*   **HTML (Hypertext Markup Language):** 
    *   **Hypertext:** Web pages ko aapas mein link karne ka tarika (links).
    *   **Markup Language:** Aap text document ko **tags** se "mark-up" karte hain taaki browser samajh sake ki content ko kaise display karna hai (heading, paragraph, list etc.).
    *   HTML complex interactivity (JS) ya styling (CSS) nahi karta, wo sirf **structure** deta hai. CSS aur JS iske upar kaam karte hain.

---

## ⚙️ 3. Features of Web Programming

Web programming ki kuch main features hain jo websites ko dynamic aur functional banati hain:

1.  **Interactivity:** User engagement badhana. (Example: Fitness app mein buttons click karke workout log karna).
2.  **Dynamic Content:** Content user actions ya external sources ke basis par change hona. (Example: Weather app jo real-time data API se lata hai).
3.  **Data Storage and Retrieval:** Data ko database mein save aur retrieve karna. (Example: Hotel booking system jahan details save hoti hain).
4.  **Server-Side Processing:** Server par code execute hona (jaise e-commerce site par total bill calculate karna aur payment process karna).
5.  **User Authentication & Security:** Sirf authorized users ko access dena (jaise Banking apps mein login verification).
6.  **API Integration:** External services ko integrate karna (jaise Google Maps API se directions lena).
7.  **Content Management (CMS):** Bina coding ke content edit karna (jaise WordPress).
8.  **Responsive Design:** Website ka alag-alag screen sizes (mobile, tablet, desktop) par fit hona. (CSS media queries se hota hai).
9.  **Cross-Browser Compatibility:** Website ka Chrome, Firefox, Safari sab par same dikhna.
10. **Collaboration and User Interaction:** Multiple users ka ek saath kaam karna (jaise Google Docs).
11. **E-commerce Functionality:** Online shopping, cart, payment, order tracking.
12. **Scalability:** Zyada traffic aane par bhi website ka smooth chalna.

---

## 🛠️ 4. Uses of HTML

HTML ka use kahan-kahan hota hai?

1.  **Development of Web Pages:** Web pages ka structure banane ke liye (tables, sections). HTML5 ke **Semantic elements** ne kaam aasan kar diya hai.
2.  **Internet Navigation:** `<a>` (anchor tag) ka use karke hyperlinks banaye jate hain jo ek page se dusre page par le jate hain. 
    *   *Example:* `<a href="india.org"> Click here to open! </a>`
3.  **Responsive Design:** `<meta>` tag aur CSS (VW unit - viewport width) ka use karke website ko har device par responsive banaya jata hai.
4.  **Creation of Web Documents (DOM):** HTML document banane ke liye. Iska structure ek tree jaisa hota hai jise **DOM (Document Object Model)** kehte hain. Root element `<html>` hota hai jiske andar `<head>` aur `<body>` aate hain.
5.  **Offline Web Applications:** Internet ke bina bhi web apps chalana. Iske liye ek **cache manifest file** banai jati hai jo browser ko batati hai ki kaunsi files offline save karni hain.
6.  **Innovative Features:** HTML5 ne naye features diye jaise dynamic headers, embedded infographics, etc. Google Chrome latest APIs ko support karta hai.
7.  **Enhancing Website's Potential:** **Native APIs** (jaise visibility, full screen, media capture) ka use karke website ki capability badhai jati hai bina page ki performance kharab kiye.

---

## 🕰️ 5. Versions of HTML

HTML ka safar (Evolution):

| Version | Year | Key Features |
| :--- | :--- | :--- |
| **HTML 1.0** | 1993 | Sabse basic. Sirf headings, lists, paragraphs, images. Koi styling ya tables nahi the. |
| **HTML 2.0** | 1995 | **Standardization** hui. Forms (text boxes, buttons) aur `<table>` tag aaya. **W3C** (World Wide Web Consortium) ki sthapna hui taaki sab browsers ek rule follow karein. |
| **HTML 3.2** | 1997 | **CSS (Cascading Style Sheets)** ka support aaya (thodi styling). Images par zyada control (align, size). International characters aaye. |
| **HTML 4.01** | 1999 | CSS file ko link karne ke liye `<link>` tag aaya. Naye tags: `<fieldset>`, `<header>`, `<footer>`. Tables mein `colspan` aur `rowspan` aaye. |
| **XHTML 1.0** | 2000 | Ye HTML ka strict version hai. XML ke rules follow karta hai (tags properly close hone chahiye). Isse browser compatibility better hui. |
| **HTML5** | 2008 (draft), 2014 (official) | Sabse latest. **Semantic tags** (`<header>`, `<footer>`, `<section>`), **Audio/Video** support, Form validations (`type="email"`, `type="password"`), aur `<figcaption>` aaye. |

---

## 💻 6. HTML Syntax & First Web Page

HTML document banane ke steps:
1.  **Editor chuno:** Notepad, VS Code, Sublime Text.
2.  **Code likho.**
3.  **File save karo:** `.html` extension ke saath (e.g., `Sample.html`).
4.  **Browser mein open karo** (double click).

### Basic HTML Code Structure (Boilerplate)
```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>
<body>
    <h1>My First Heading</h1>
    <p>My first paragraph.</p>
</body>
</html>
```

**Explanation of Tags:**
*   `<!DOCTYPE html>`: Batata hai ki ye HTML5 document hai.
*   `<html>`: Root element (poore document ka base).
*   `<head>`: Meta information (jo screen par nahi dikhti, jaise title).
*   `<title>`: Browser ke tab par dikhne wala naam.
*   `<body>`: Jo bhi content screen par dikhega (headings, paragraphs, images).
*   `<h1>`: Heading (bada size).
*   `<p>`: Paragraph.

> [!NOTE]
> **HTML Element:** Start tag + Content + End tag. (e.g., `<h1>Heading</h1>`)
> **Empty Elements:** Jinme content nahi hota aur end tag nahi lagta. Example: `<br>` (line break), `<hr>` (horizontal line).

---

## 🏗️ 7. Head and Body Sections of HTML

### 7.1 `<head>` Tag (Document ki Meta Information)
Ye container tag hai jo document ke baare mein information rakhta hai (jo user ko screen par nahi dikhti).

**Iske andar kya aata hai?**
1.  `<title>`: Page ka title (browser tab par).
2.  `<meta>`: Metadata (character encoding, description, keywords, author).
3.  `<link>`: External stylesheet (CSS) ya icon attach karna.
4.  `<style>`: Internal CSS likhna.
5.  `<script>`: JavaScript code attach karna.

> [!WARNING]
> **Deprecated Attribute:** `profile` attribute pehle use hota tha meta profiles link karne ke liye, par ab HTML5 mein ise remove (deprecated) kar diya gaya hai.

**Example:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>HTML Head Tag</title>
</head>
<body>
    <p>Computer science is my Favourite subject</p>
    <hr>
</body>
</html>
```

### 7.2 `<body>` Tag (Visible Content)
Isme wo saara content aata hai jo user browser mein dekhta hai. Jaise text, images, links, forms.

**Common Tags inside Body:**
*   `<h1>` to `<h6>`: Headings.
*   `<p>`: Paragraphs.
*   `<img>`: Images (src = source, alt = alternative text).
*   `<a>`: Links.

> [!WARNING]
> **Deprecated Attributes of Body (HTML5 mein nahi chalte):**
> *   `background` (URL of background image)
> *   `bgcolor` (Background color)
> *   `alink` (Active link color)
> *   `link` (Link color)
> *   `text` (Text color)
> *   `vlink` (Visited link color)
> (Aajkal ye sab CSS se kiya jata hai).

---

## 📝 8. Quick Revision (Q&A)

**Q1. What does API integration enable?**
*   *Ans:* Ye websites ko external services (jaise Google Maps, Weather APIs) se connect karke unka data use karne ki facility deta hai.

**Q2. What does CMS stand for?**
*   *Ans:* Content Management Systems (jaise WordPress), jisse bina coding ke content manage kiya jata hai.

**Q3. What does responsive design ensure?**
*   *Ans:* Website ka har device (mobile, tablet, desktop) par screen size ke hisaab se automatically adjust ho jana.

**Q4. What is the purpose of the `<head>` section in an HTML document?**
*   *Ans:* Ye metadata, page title, aur external resources (CSS/JS) ko contain karta hai, jo visible content ko render karne mein help karte hain.

**Q5. What is the significance of the "viewport width" (VW) unit?**
*   *Ans:* Ye text content ko device ki screen width ke hisaab se responsive banane ke liye use hota hai.

**Q6. What technology empowers designers to enhance the visual appeal?**
*   *Ans:* CSS (Cascading Style Sheets).

**Q7. Which HTML attribute is used to specify the language of the content?**
*   *Ans:* `lang` attribute (jaise `<html lang="en">`).

**Q8. What is an HTML element?**
*   *Ans:* Ek start tag, content, aur end tag ka combination. (e.g., `<p>Hello</p>`).

**Q9. What are empty elements?**
*   *Ans:* Jinme content nahi hota aur end tag nahi lagta (jaise `<br>`, `<hr>`, `<img>`).

**Q10. HTML 4.01 aur XHTML 1.0 mein kya difference hai?**
*   *Ans:* XHTML 1.0, HTML 4.01 ka strict version hai jo XML rules follow karta hai (tags properly close hone chahiye, case-sensitive hota hai).

---
> **💡 Bhai ka Gyan:** Exam mein HTML5 ke naye features (Semantic tags, Audio/Video) aur HTML ke versions ka timeline bahut important hai. Aur Basic Structure (`<!DOCTYPE html>` to `</html>`) likhna zarur aana chahiye!
