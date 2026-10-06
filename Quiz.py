import streamlit as st

if "subject_scores" not in st.session_state:
    st.session_state.subject_scores = {}

st.title("Online Quiz Portal")

if st.button("Reset Quiz"):
    st.session_state.clear()
    st.rerun()

rollno = st.text_input("Roll Number")

if rollno:
    st.success(f"Welcome {rollno}")

    subject = st.radio(
        "Select Subject",
        ["Python", "English", "Maths"],
        index=None,
        horizontal=True
    )
    st.divider()

    if subject == "Python":
        st.subheader("Python Quiz")

        q1 = st.radio(
            "1. Which symbol is used for comments?",
            ["//", "*", "$", "#"],
            index=None
        )
        q2 = st.radio(
            "2. Which function is used to read data from the user?",
            ["print()", "display()", "read()", "input()"],
            index=None
        )
        q3 = st.radio(
            "3. Which keyword is used to define a function in Python?",
            ["fun", "def", "import", "define"],
            index=None
        )
        q4 = st.radio(
            "4. Which data type is used to store a sequence of characters?",
            ["int", "float", "str", "bool"],
            index=None
        )
        q5 = st.radio(
            "5. Which operator is used for exponentiation in Python?",
            ["*", "**", "//", "%"],
            index=None
        )

        answers = [
            q1 == "#",
            q2 == "input()",
            q3 == "def",
            q4 == "str",
            q5 == "**"
        ]

        if st.button("Submit Quiz"):
            score = sum(answers)
            st.session_state.subject_scores["Python"] = score
            st.success("Your Result")
            st.write(f"Roll Number: {rollno}")
            st.write(f"Selected Subject: {subject}")
            st.metric("Your Score", f"{score}/5")

            if score == 5:
                st.balloons()
                st.success("Excellent")
            elif score >= 3:
                st.success("Good job!")
            else:
                st.warning("Keep Practicing!")

    elif subject == "English":
        st.subheader("English Quiz")

        q1 = st.radio(
            "1. Which word is a noun?",
            ["Run", "Happily", "Book", "Quickly"],
            index=None
        )
        q2 = st.radio(
            "2. Choose the correct plural form of 'child'.",
            ["Childs", "Children", "Childes", "Childer"],
            index=None
        )
        q3 = st.radio(
            "3. Which sentence is grammatically correct?",
            ["She go to school every day.", "She goes to school every day.", "She going to school every day.", "She gone to school every day."],
            index=None
        )
        q4 = st.radio(
            "4. Which word is the opposite of 'beautiful'?",
            ["Ugly", "Pretty", "Lovely", "Bright"],
            index=None
        )
        q5 = st.radio(
            "5. Identify the adjective in the sentence: 'The red apple is sweet.'",
            ["apple", "sweet", "is", "the"],
            index=None
        )

        answers = [
            q1 == "Book",
            q2 == "Children",
            q3 == "She goes to school every day.",
            q4 == "Ugly",
            q5 == "sweet"
        ]

        if st.button("Submit Quiz"):
            score = sum(answers)
            st.session_state.subject_scores["English"] = score
            st.success("Your Result")
            st.write(f"Roll Number: {rollno}")
            st.write(f"Selected Subject: {subject}")
            st.metric("Your Score", f"{score}/5")

            if score == 5:
                st.balloons()
                st.success("Excellent")
            elif score >= 3:
                st.success("Good job!")
            else:
                st.warning("Keep Practicing!")

    elif subject == "Maths":
        st.subheader("Maths Quiz")

        q1 = st.radio(
            "1. What is 12 x 5?",
            ["50", "60", "70", "72"],
            index=None
        )
        q2 = st.radio(
            "2. What is 25 + 17?",
            ["32", "42", "40", "38"],
            index=None
        )
        q3 = st.radio(
            "3. What is the value of 9^2?",
            ["18", "72", "81", "90"],
            index=None
        )
        q4 = st.radio(
            "4. Which is the smallest prime number?",
            ["0", "1", "2", "3"],
            index=None
        )
        q5 = st.radio(
            "5. What is 100 / 4?",
            ["20", "25", "30", "35"],
            index=None
        )

        answers = [
            q1 == "60",
            q2 == "42",
            q3 == "81",
            q4 == "2",
            q5 == "25"
        ]

        if st.button("Submit Quiz"):
            score = sum(answers)
            st.session_state.subject_scores["Maths"] = score
            st.success("Your Result")
            st.write(f"Roll Number: {rollno}")
            st.write(f"Selected Subject: {subject}")
            st.metric("Your Score", f"{score}/5")

            if score == 5:
                st.balloons()
                st.success("Excellent")
            elif score >= 3:
                st.success("Good job!")
            else:
                st.warning("Keep Practicing!")

    if st.session_state.subject_scores:
        total_score = sum(st.session_state.subject_scores.values())
        st.divider()
        st.subheader("Overall Progress")
        st.metric("Total Score", f"{total_score}/15")
        for subject_name, score in st.session_state.subject_scores.items():
            st.write(f"{subject_name}: {score}/5")

else:
    st.info("Please Enter roll no")