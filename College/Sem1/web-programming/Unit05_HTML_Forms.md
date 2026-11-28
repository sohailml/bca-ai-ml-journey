# 📝 Web Programming - Unit 5: HTML Forms

> **Course:** BCA - Semester 1  
> **Topic:** HTML Forms, Form Elements, Input Types, Form Attributes

---

## 📑 Table of Contents
1. [Introduction to HTML Forms](#-1-introduction-to-html-forms)
2. [Form Elements (11 Types)](#-2-form-elements-11-types)
3. [Form Input Types (22 Types)](#-3-form-input-types-22-types)
4. [Form Attributes (Complete)](#-4-form-attributes-complete)
5. [GET vs POST (Exam Important)](#-5-get-vs-post-exam-important)
6. [Form Validation & Security (Extra Exam Topic)](#-6-form-validation--security-extra-exam-topic)
7. [Summary, Cheat Sheet & Q&A](#-7-summary-cheat-sheet--qa)

---

## 📌 1. Introduction to HTML Forms

HTML `<form>` element ek **container** ki tarah kaam karta hai jisme hum input fields (text, email, password), checkboxes, radio buttons, aur submit buttons rakh sakte hain. Iska main kaam **user se data lena aur server ko bhejna** hota hai.

*   **Real-world Example:** Online shopping karte waqt address form bharna aur phir payment form bharna.
*   **Flexibility:** Forms ko paragraphs, lists, ya tables ke andar rakh sakte hain taaki design accha lage.

**Learning Objectives:**
*   Form ke basic components identify karna.
*   Block-level vs Inline-level form elements mein difference samajhna.
*   Alag-alag input types se form banana.
*   Form attributes ka behavior samajhna.
*   GET vs POST ke security implications evaluate karna.

---

## 🧩 2. Form Elements (11 Types)

`<form>` element ke andar ye 11 elements use ho sakte hain:

| Element | Kaam | Example |
| :--- | :--- | :--- |
| **`<form>`** | Form ka container. `action` (kahan bhejna hai) aur `method` (GET/POST) define karta hai. | `<form action="process.php" method="POST">` |
| **`<input>`** | Sabse versatile element. `type` attribute se text, password, radio, checkbox etc. ban jata hai. | `<input type="text" name="username">` |
| **`<label>`** | Input field ka text label. `for` attribute se input ke `id` se connect hota hai (accessibility ke liye). | `<label for="name">Name:</label>` |
| **`<select>`** | Dropdown list banata hai. | `<select name="city">...</select>` |
| **`<textarea>`** | Multi-line text input (comments, address ke liye). | `<textarea rows="4" cols="50"></textarea>` |
| **`<button>`** | Clickable button (submit, reset, ya JavaScript trigger). | `<button type="submit">Submit</button>` |
| **`<fieldset>`** | Related form elements ko group karta hai (visual box banata hai). | `<fieldset>...</fieldset>` |
| **`<legend>`** | `<fieldset>` ke andar title/caption deta hai. | `<legend>Personal Info</legend>` |
| **`<datalist>`** | `<input>` ke saath use hota hai. Predefined suggestions deta hai (autocomplete). | `<input list="browsers"><datalist id="browsers">...</datalist>` |
| **`<output>`** | Calculation ka result display karta hai (JavaScript ke saath). | `<output name="result">0</output>` |
| **`<option>`** | `<select>` ke andar individual option. | `<option value="delhi">Delhi</option>` |
| **`<optgroup>`** | `<select>` ke andar related options ko group karta hai. | `<optgroup label="India">...</optgroup>` |

**Basic Form Syntax:**
```html
<form action="processing-script-url" method="GET/POST">
    <!-- Form controls go here -->
</form>
```

---

## 🎛️ 3. Form Input Types (22 Types)

`<input>` element ka `type` attribute change karke alag-alag controls banaye ja sakte hain:

| Input Type | Kaam | Example |
| :--- | :--- | :--- |
| **`text`** | Single-line text input. | `<input type="text" name="username">` |
| **`password`** | Text hide karke dots dikhata hai. | `<input type="password" name="pass">` |
| **`email`** | Email address input (built-in validation). | `<input type="email" name="email" required>` |
| **`number`** | Numeric input (min, max, step). | `<input type="number" min="1" max="100">` |
| **`radio`** | Ek group mein se ek option select karna. | `<input type="radio" name="gender" value="male">` |
| **`checkbox`** | Multiple options select karna. | `<input type="checkbox" name="hobby" value="reading">` |
| **`date`** | Date picker. | `<input type="date" name="dob">` |
| **`time`** | Time picker. | `<input type="time" name="appt">` |
| **`datetime-local`** | Date + Time dono. | `<input type="datetime-local" name="meeting">` |
| **`month`** | Month + Year select karna. | `<input type="month" name="month">` |
| **`week`** | Week + Year select karna. | `<input type="week" name="week">` |
| **`color`** | Color picker. | `<input type="color" name="color">` |
| **`range`** | Slider control (numeric range). | `<input type="range" min="0" max="100">` |
| **`file`** | File upload control. | `<input type="file" name="file">` |
| **`hidden`** | User ko nahi dikhta, server ko data bhejne ke liye. | `<input type="hidden" name="token" value="abc123">` |
| **`image`** | Image ko submit button ki tarah use karna. | `<input type="image" src="submit.png" alt="Submit">` |
| **`search`** | Search query ke liye optimized text field. | `<input type="search" name="q">` |
| **`tel`** | Telephone number input. | `<input type="tel" name="phone">` |
| **`url`** | Website URL input (built-in validation). | `<input type="url" name="website">` |
| **`submit`** | Form submit karne ka button. | `<input type="submit" value="Submit">` |
| **`reset`** | Form fields ko default values par reset karna. | `<input type="reset" value="Reset">` |
| **`button`** | Generic button (JavaScript trigger karne ke liye). | `<input type="button" value="Click" onclick="...">` |

**Full Example (PDF):**
```html
<form action="#" method="post">
    <label for="text">Text Input:</label>
    <input type="text" id="text" name="text"><br>
    
    <label for="password">Password Input:</label>
    <input type="password" id="password" name="password"><br>
    
    <label>Radio Buttons:</label>
    <input type="radio" id="male" name="gender" value="male">
    <label for="male">Male</label>
    <input type="radio" id="female" name="gender" value="female">
    <label for="female">Female</label><br>
    
    <label>Checkboxes:</label>
    <input type="checkbox" id="subscribe" name="subscription" value="yes">
    <label for="subscribe">Subscribe</label><br>
    
    <label for="number">Number Input:</label>
    <input type="number" id="number" name="number" min="1" max="100" step="1"><br>
    
    <label for="email">Email Input:</label>
    <input type="email" id="email" name="email"><br>
    
    <label for="date">Date Input:</label>
    <input type="date" id="date" name="date"><br>
    
    <label for="time">Time Input:</label>
    <input type="time" id="time" name="time"><br>
    
    <label for="color">Color Input:</label>
    <input type="color" id="color" name="color"><br>
    
    <label for="file">File Upload:</label>
    <input type="file" id="file" name="file"><br>
    
    <input type="hidden" id="hidden" name="hidden" value="hidden-value">
    <input type="submit" id="submit" value="Submit Form">
</form>
```

---

## ⚙️ 4. Form Attributes (Complete)

PDF mein diye gaye saare attributes + jo cut ho gaye wo bhi:

| Attribute | Kaam | Values | Example |
| :--- | :--- | :--- | :--- |
| **`action`** | Form data kahan bhejna hai (URL). | URL path | `action="process.php"` |
| **`method`** | Data kaise bhejna hai. | `GET` ya `POST` | `method="POST"` |
| **`name`** | Form ka naam (multiple forms identify karne ke liye). | String | `name="registrationForm"` |
| **`target`** | Server response kahan dikhana hai. | `_blank`, `_self`, `_parent`, `_top` | `target="_blank"` |
| **`enctype`** | Data encoding ka tarika. | `application/x-www-form-urlencoded` (default), `multipart/form-data` (file upload), `text/plain` | `enctype="multipart/form-data"` |
| **`autocomplete`** | Browser auto-fill kare ya nahi. | `on`, `off` | `autocomplete="on"` |
| **`novalidate`** | Browser validation disable karna. | (Boolean) | `<form novalidate>` |
| **`onsubmit`** | Form submit hone par JavaScript function call karna. | JS function | `onsubmit="return validateForm()"` |
| **`onreset`** | Form reset hone par JavaScript function call karna. | JS function | `onreset="resetForm()"` |

**Example (File Upload):**
```html
<form action="upload.php" method="post" enctype="multipart/form-data">
    <input type="file" name="myfile">
    <input type="submit" value="Upload">
</form>
```

---

## ⚖️ 5. GET vs POST (Exam Important)

Ye sabse zyada pucha jane wala question hai. Dono methods ka comparison:

| Feature | GET | POST |
| :--- | :--- | :--- |
| **Data Visibility** | Data URL mein dikhta hai (query string). | Data request body mein hidden rehta hai. |
| **Security** | Kam secure (URL history mein save hota hai). | Zyada secure (sensitive data ke liye). |
| **Data Limit** | Limited (URL ki length ~2048 characters). | Unlimited (large data bhej sakte hain). |
| **Caching** | Browser cache kar sakta hai. | Cache nahi hota. |
| **Bookmark** | Bookmark kiya ja sakta hai. | Bookmark nahi kiya ja sakta. |
| **Use Case** | Search queries, filters, public data. | Login, payment, file upload, sensitive data. |
| **Idempotent** | Haan (same request same result). | Nahi (POST se data change ho sakta hai). |

> [!WARNING]
> **Exam Trap:** GET se password kabhi mat bhejo, kyunki wo URL mein dikhta hai aur history mein save ho jata hai. Sensitive data ke liye hamesha POST use karo.

---

## 🔒 6. Form Validation & Security (Extra Exam Topic)

PDF mein validation ka chhota sa mention hai, par exams mein detail aata hai.

### 6.1 Client-side Validation
*   **Kahan hoti hai?** Browser mein.
*   **Kaise?** HTML attributes (`required`, `pattern`, `min`, `max`, `type="email"`) ya JavaScript se.
*   **Fayda:** Instant feedback, server load kam.
*   **Nuksan:** Bypass ho sakti hai (browser mein JavaScript off karke).

### 6.2 Server-side Validation
*   **Kahan hoti hai?** Server par (PHP, Python, Java).
*   **Kaise?** Server script data ko check karti hai.
*   **Fayda:** Secure, bypass nahi ho sakti.
*   **Nuksan:** Slow feedback.

> [!IMPORTANT]
> **Security Rule:** Dono validations use karo. Client-side UX ke liye, Server-side security ke liye.

### 6.3 Security Issues (Exam Special)
1.  **SQL Injection:** User input ke through malicious SQL code bhejna. (Prevention: Prepared statements)
2.  **Cross-Site Scripting (XSS):** Malicious JavaScript code inject karna. (Prevention: Input sanitization)
3.  **CSRF (Cross-Site Request Forgery):** User ke session ka misuse. (Prevention: CSRF tokens)
4.  **File Upload Vulnerabilities:** Malicious files upload karna. (Prevention: File type validation)

---

## 📝 7. Summary, Cheat Sheet & Q&A

### 7.1 Summary
*   **Form:** User input lene aur server ko bhejne ka container.
*   **Elements:** `<input>`, `<label>`, `<select>`, `<textarea>`, `<button>`, `<fieldset>`, `<legend>`, `<datalist>`, `<output>`, `<option>`, `<optgroup>`.
*   **Input Types:** 22 types (text, password, email, number, radio, checkbox, date, file, hidden, etc.).
*   **Attributes:** `action`, `method`, `name`, `target`, `enctype`, `autocomplete`, `novalidate`, `onsubmit`.
*   **GET vs POST:** GET URL mein data bhejta hai (kam secure), POST body mein (zyada secure).
*   **Validation:** Client-side (browser) + Server-side (server) dono zaroori.

### 7.2 Cheat Sheet

```markdown
| Concept | Key Point |
|---------|-----------|
| Form Container | `<form action="URL" method="POST">` |
| Text Input | `<input type="text" name="username">` |
| Password | `<input type="password">` |
| Radio | `<input type="radio" name="gender">` (same name) |
| Checkbox | `<input type="checkbox" name="hobby">` (multiple) |
| Dropdown | `<select><option>...</option></select>` |
| File Upload | `<input type="file">` + `enctype="multipart/form-data"` |
| Submit | `<input type="submit">` ya `<button type="submit">` |
| GET | URL mein data, search ke liye |
| POST | Body mein data, login/payment ke liye |
| Validation | Client (HTML/JS) + Server (PHP/Java) |
```

### 7.3 Self-Assessment Questions (PDF Answers)
*Note: PDF mein SAQs ke answers cut hain, par yahan standard answers diye hain.*

1.  **What is the purpose of the `<form>` element?** To collect user input and send it to a server for processing.
2.  **Which attribute specifies where form data is sent?** `action`.
3.  **Which attribute specifies how form data is sent?** `method`.
4.  **What are the two common methods for form submission?** GET and POST.
5.  **Which input type hides the entered text?** `password`.
6.  **Which input type is used for multiple selections from a list?** `checkbox`.
7.  **Which input type allows only one selection from a group?** `radio`.
8.  **What is the purpose of the `<label>` element?** To provide a text label for form controls, improving accessibility.
9.  **How do you associate a `<label>` with an `<input>`?** Using the `for` attribute (label) and `id` attribute (input).
10. **Which attribute is used for file uploads?** `enctype="multipart/form-data"`.

### 7.4 Terminal Questions (Hints)
1.  **Create a registration form with name, email, password, gender, and hobbies.** (Use `<input type="text">`, `type="email"`, `type="password">`, `type="radio">`, `type="checkbox">`)
2.  **Explain GET vs POST with examples.** (Refer Section 5)
3.  **What is client-side vs server-side validation?** (Refer Section 6)
4.  **Write HTML code for a file upload form.** (Use `enctype="multipart/form-data"`)
5.  **What are the security implications of HTML forms?** (SQL Injection, XSS, CSRF - Refer Section 6.3)

### 7.5 Extra Practice Questions (Exam Special)
1.  Write the HTML code to create a login form (username + password).
2.  Differentiate between `type="submit"` and `type="button"`.
3.  What is the use of the `hidden` input type?
4.  Explain the `autocomplete` attribute.
5.  What happens if you don't specify the `action` attribute in a form?

---
> **💡 Bhai ka Gyan:** Exam mein **GET vs POST**, **Input Types (radio, checkbox, password)**, aur **Form Attributes (`action`, `method`, `enctype`)** ke questions pakke aate hain. File upload ke liye `enctype="multipart/form-data"` yaad rakhna. Client-side vs Server-side validation ka difference bhi important hai. All the best! 🚀
