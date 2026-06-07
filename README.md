# 🐧 Ajin T's AI English Class Portfolio with Edutech

This repository contains the source code for an **EdTech-Integrated Jigsaw Cooperative Reading Web Application** tailored for Middle School 2nd-grade English classes. Built on the Streamlit framework, this application integrates vocabulary gamification, comprehension quizzes, a classroom timer, and a multimedia resource repository into a single unified web interface.

---

## 🎯 1. App Purpose & Educational Objectives

* **Support Self-Paced & Differentiated Learning**: Provides individual students with an engaging environment for vocabulary retrieval practice and formative self-assessment according to their own learning pace.
* **Facilitate Interaction-Driven Cooperative Learning**: Acts as a scaffolding and verification tool during Jigsaw activities, supporting peer-to-peer oral information transfer.
* **Minimize Classroom Transition Time (All-in-One)**: Centralizes essential resources—such as digital worksheets, video streams, and a visual timer—under a single URL, eliminating technical friction and optimizing classroom time management.

---

## 🏫 2. Curriculum & Class Information

* **Target Level**: Middle School 2nd Grade (South Korea)
* **Lesson Topic**: Humpback Whale Observation Journal (Reading)
* **Period**: 2nd out of 8 periods (2/8 차시 - Reading & Cooperation Focus)
* **Textbook**: Cheonjae under 2022 revised national curriculum (Published 2026)
* **Instructional Model**: Jigsaw II Cooperative Reading + AI EdTech Integration

---

## 📋 3. 45-Minute Lesson Plan & EdTech Integration Points

### 📊 Lesson Procedure at a Glance

| Phase | Time | Learning Activities & Tasks | ✨ EdTech & Material Integration |
| :--- | :--- | :--- | :--- |
| **Introduction** | 5 min. | Attendance check & Vocabulary review game | **01 🕹️ Word Game App** |
| **Development 1** | 5 min. | Pre-reading: Video-based prompt & Topic inference | **05 🎬 In-class Video** |
| **Development 2** | 12 min. | Jigsaw Phase 1: Individual segment scanning | **03 📘 Textbook** & **04 📝 Worksheet** |
| **Development 3** | 10 min. | Jigsaw Phase 2: Peer sharing & Oral synthesis | Offline peer tutoring (**06 ⏳ Class Timer** for pacing) |
| **Development 4** | 8 min. | Text validation & Differentiated assessment | **02 📖 Quiz App** |
| **Conclusion** | 5 min. | Wrap-up, qualitative feedback, & Next-class preview | Physical Board & Teacher-led feedback |

---

## 🕹️ 4. Core Features & User Manual

### [01] 🕹️ Word Game App 
* **Classroom Implementation**: Introduction Phase (4 min.)
* **How to Use**:
  1. Students log in by entering their names and clicking the `Start` button.
  2. English words drop from the top of the canvas. Students must type the correct Korean meaning before the words hit the bottom to score points.
  3. Upon Game Over, clicking the `📚 단어학습하기` (Word Study) button unlocks a **Digital Self-Diagnostic Worksheet** where students can practice spelling and listen to standard American accents powered by the gTTS engine.

### [02] 📖 Quiz App 
* **Classroom Implementation**: Development Phase 4 (8 min.) - Designed for Fast-Finishers.
* **How to Use**:
  1. Students who complete the reading verification early access this page via QR code or the sidebar menu.
  2. They solve 15 text-based reading comprehension questions.
  3. The real-time scoring engine provides immediate feedback, allowing students to access a specialized review mode with detailed linguistic and contextual explanations.

### [03] 📘 Textbook & [04] 📝 Worksheet 
* **How to Use**: To bypass rigid browser-side CORS policies, these pages offer large, touch-friendly, high-speed download triggers. Students can securely download `textbook.pdf` and `worksheet.pdf (Research Note)` straight onto their tablets or smartphones with a single tap.

### [05] 🎬 In-class Video 
* **How to Use**: Implements a lightweight YouTube unlisted video streaming architecture. It ensures zero-buffering, high-definition playback of the humpback whale introductory clip, even when multiple student devices hit the server simultaneously.

### [06] ⏳ Class Timer 
* **How to Use**: A teacher-facing utility projected onto the main classroom screen. It synchronizes with Korea Standard Time (KST) and utilizes JavaScript canvas modules to display a dynamic, circular countdown ring for Jigsaw phases (12 min. / 10 min.), triggering an audio alarm once time expires.

---
*Developed by Ajin T (Namyang Middle School)*
