# 🐧 Ahjin T's AI Fusion English Class Portfolio

This repository contains the source code for an **EdTech-Integrated Jigsaw Cooperative Reading Web Application** tailored for Middle School 2nd-grade English classes. Built on the Streamlit framework, this application integrates vocabulary gamification, comprehension quizzes, a classroom timer, and a multimedia resource repository into a single unified web interface.

---

## 🏫 1. Teaching Context

* **Learners Profile**: The target learners are 2nd-grade middle school students in South Korea (mixed-ability, approximately 20 students per class). 
* **Classroom Environment**: The class takes place in a smart-classroom setting where every student is equipped with an individual digital device (tablet or smartphone) and high-speed wireless internet access. A main projector screen is available at the front for teacher-led demonstrations.
* **Learners' Challenges**: 
  * **Linguistic Heterogeneity**: There is a significant gap between fast-finishers (advanced learners) and underachieving students in terms of reading fluency and core vocabulary retrieval.
  * **Cognitive Load & Passive Reading**: Students often exhibit low engagement and high cognitive fatigue when reading longer informational texts in English.
  * **Oral Communication Anxiety**: Many students struggle to synthesize and orally explain English texts to their peers due to an unsupportive environment or a lack of interactive scaffolding.

---

## 🎯 2. Lesson Purpose

* **What it Teaches**: This lesson focuses on a **Humpback Whale Observation Journal** (Reading domain). It explicitly trains students to scan for specific information, synthesize fragmented text portions, and accurately document informational details through peer tutoring.
* **Why it is Meaningful**: Rather than relying on traditional, teacher-centered translation methods, this lesson adopts the **Jigsaw II cooperative learning model**. It transforms reading into an active, communicative task. Students are held individually accountable for their assigned segments, which fosters positive interdependence and encourages empathetic peer-to-peer tutoring in an EFL (English as a Foreign Language) context.

---

## 🚀 3. App Purpose

* **Why it was Built**: This application was developed to centralize all digital and multimedia resources required for the Jigsaw lesson into a single web URL, mitigating the technical friction typically caused by moving between multiple third-party apps.
* **Learning Needs Addressed**:
  * **Immediate Vocabulary Retrieval**: The word game addresses the need for dynamic, low-stakes formative retrieval practice at the beginning of class.
  * **Scaffolding for Fast-Finishers**: The interactive quiz meets the learning needs of advanced students by providing meaningful, self-paced extension activities while the teacher scaffolds struggling groups.
  * **CORS & Device Compatibility**: Centralized download triggers solve persistent browser-level security blockages (CORS policies), enabling seamless PDF and media access across all student operating systems.

---

## 📐 4. App Design

* **How it Works**: The app utilizes a Streamlit multipage navigation architecture (`st.navigation`). It isolates distinct lesson assets into clean, separate sub-pages accessible via a left-hand sidebar menu, keeping student focus contained within a single ecosystem.
* **Data & Content Utilized**:
  * **Text/CSV**: Structured vocabulary datasets (`data.csv`) and reading comprehension items (`quizdata.csv`) containing 15 multi-level questions with linguistic explanations.
  * **Media**: Unlisted high-definition video streaming APIs (YouTube) for zero-buffering playback and standard PDF binary streams for educational worksheets.
  * **Libraries**: Python-based standard processing engines, including `gTTS` (Google Text-to-Speech) for on-demand American accent generation, and a JavaScript-driven canvas for dynamic UI rendering.
* **Learner Interaction**: Students input text for game answers, submit strings for identity tracking, toggle interactive radio buttons for comprehension checks, play localized audio files for pronunciation, and trigger responsive download modules.

---

## 📋 5. 45-Minute Lesson Plan & Classroom Use

### 📊 Lesson Procedure at a Glance

| Phase | Time | Learning Activities & Tasks | 🕹️ App Implementation & Improvements |
| :--- | :--- | :--- | :--- |
| **Introduction** | 5 min. | Attendance check & Vocabulary review game | **01 🕹️ Word Game App**<br>• *Improves engagement and vocabulary retention through low-stakes gamification.* |
| **Development 1** | 5 min. | Pre-reading: Video-based prompt & Topic inference | **05 🎬 In-class Video** (YouTube Stream)<br>• *Activates schema without browser-side blocking or buffering.* |
| **Development 2** | 12 min. | Jigsaw Phase 1: Individual segment scanning | **03 📘 Textbook** & **04 📝 Worksheet**<br>• *Ensures instant, cross-platform PDF material distribution.* |
| **Development 3** | 10 min. | Jigsaw Phase 2: Peer sharing & Oral synthesis | Offline interaction aided by **06 ⏳ Class Timer**<br>• *Improves time awareness and keeps group tasks on track.* |
| **Development 4** | 8 min. | Text validation & Differentiated assessment | **02 📖 Quiz App**<br>• *Provides advanced learners with automated assessment and instant meta-cognitive feedback.* |
| **Conclusion** | 5 min. | Wrap-up, qualitative feedback, & Next-class preview | Physical Board & Teacher-led feedback<br>• *Consolidates learning outcomes and rewards collaboration.* |

---

## ⚠️ 6. Limitations

* **Lack of Real-time Teacher Dashboard**: Student scores from the Word Game and Comprehension Quiz are computed locally within individual sessions. The teacher cannot monitor real-time class metrics or collect formative data concurrently without manually checking student screens.
* **Static Vocabulary Pool**: The vocabulary game draws from a predefined, static CSV file, meaning it lacks an adaptive mechanism to adjust word-dropping speeds or difficulty levels based on individual student performance.
* **Dependency on Client-Side Hardware**: Features like the gTTS audio playback rely heavily on the student device's native browser handling, which can occasionally lead to audio lag on older mobile models.

---

## 🔮 7. Future Development

* **Database & LRS Integration**: Future versions will integrate a lightweight cloud database (such as Google Sheets API or Firestore) to log student scores, wrong answer frequencies, and time-stamps, creating a comprehensive formative assessment dashboard for the instructor.
* **Adaptive Learning Algorithm**: I plan to implement an item-response theory or adaptive speed algorithm in the Word Game component, tailoring the difficulty dynamically to support underachieving students.
* **AI-Powered Speaking Feedback**: I aim to expand the portfolio by adding a speech-to-text (STT) feedback loop within the Jigsaw phase to evaluate and support students' oral output accuracy in real time.

---
*Developed by Ahjin T (Namyang Middle School)*
