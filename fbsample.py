import streamlit as st
import csv
import os
import pandas as pd
#i used this to read the question file
def questionsA():
    quest = []
    with open('ass2questionA.txt', 'r') as t:
        for line in t:
            q = line.strip().split(':')
            if len(q) >= 8:
                quest.append({'question_no': q[0], 'question': q[1],'image':q[2], 'options': [q[3], q[4], q[5], q[6]], 'answer': q[7]})
    return quest
#i used this to show the question paper
def questionpaper():
    st.write(f"Question No : {st.session_state.que['question_no']}")
    st.session_state.image=st.session_state.que['image']
    if st.session_state.image != '':
        st.image(st.session_state.image)
    st.write(st.session_state.que['question'])
    st.session_state.usinp_ans=st.radio('select: ', st.session_state.que['options'],key=f'que_ind{page_no}').strip()
#i used this to append the name,scores,and answers in the csv
def result_csv():
    if 'data_exist' not in st.session_state:
        fil = os.path.exists('fb.csv')
        with open('fb.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            if not fil:
                writer.writerow(['Name', 'q1', 'q2', 'q3', 'q4', 'Score'])
            if st.session_state.name not in st.session_state.result:
                writer.writerow([st.session_state.name, st.session_state.q1, st.session_state.q2, st.session_state.q3,
                                 st.session_state.q4, st.session_state.count])
        st.session_state.data_exist = True

if 'quizAB' not in st.session_state:
    st.session_state.quizAB = questionsA()
if 'count' not in st.session_state:
    st.session_state.count = 0
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if st.session_state.page == 'home':
    st.title('WELCOME TO FOOD BEVERAGE QUIZ')
    st.image("fb.jpg",width=700)
    name = st.text_input('please enter your name : ')

    if 'name' not in st.session_state:
        st.session_state.name = name
    if st.button('Start Quiz'):
        if name:
            st.session_state.name = name
            st.session_state.result = []
            if 'page_no' not in st.session_state:
                st.session_state.page_no = 0
            if 'q1' not in st.session_state:
                st.session_state.q1 = ''
            if 'q2' not in st.session_state:
                st.session_state.q2 = ''
            if 'q3' not in st.session_state:
                st.session_state.q3 = ''
            if 'q4' not in st.session_state:
                st.session_state.q4 = ''
            st.session_state.page = 'main_app'
            st.rerun()

        else:
            st.warning('please enter your name to start quiz. ')

elif st.session_state.page == 'main_app':
    st.title('MALAYSIAN FOOD QUIZ')
    st.subheader(f"student name : {st.session_state.name}")

    quiz=st.session_state.quizAB
    page_no=st.session_state.page_no
    st.session_state.que=quiz[page_no]
    questionpaper()

    if page_no>0:
        if st.button('previous'):
            st.session_state.page_no-=1
            st.session_state.count-=1
            st.rerun()
    if page_no<len(quiz)-1:
        if st.button('next'):
            cqpno=f'q{page_no+1}'
            st.session_state[cqpno]=st.session_state.usinp_ans

            if st.session_state.usinp_ans==(st.session_state.que['answer']).strip():
                st.session_state.count+=1
                stat='correct'
            else:
                stat='wrong'
            if st.session_state.name not in st.session_state.result:
                st.session_state.result.append({'question': st.session_state.que['question_no'], 'your answer': st.session_state.usinp_ans,'correct answer': st.session_state.que['answer'], 'status': stat})
            st.session_state.page_no+=1
            st.rerun()

    if page_no==len(quiz)-1:
        if st.button('submit'):
            cqpno = f'q{page_no+1}'
            st.session_state[cqpno] = st.session_state.usinp_ans
            if st.session_state.usinp_ans==(st.session_state.que['answer']).strip():
                st.session_state.count=st.session_state.count+1
                stat='correct'
            else:
                stat='wrong'
            if st.session_state.name not in st.session_state.result:
                st.session_state.result.append({'question': st.session_state.que['question_no'], 'your answer': st.session_state.usinp_ans,'correct answer': st.session_state.que['answer'], 'status': stat})
            st.session_state.page = 'result_page'
            st.rerun()

    if st.button('back to home'):
        st.session_state.page = 'home'
        st.rerun()


elif st.session_state.page == 'result_page':
    st.write('lets see your result')
    st.subheader(f"Hello {st.session_state.name}")
    st.dataframe(st.session_state.result)
    st.write(f'your score is {st.session_state.count}')
    st.write('thank you for taking the quiz')
    if st.button('show summary'):
        st.session_state.page = 'summary_page'
        st.rerun()
    if st.button('Quit'):
        result_csv()
        st.session_state.clear()
        st.session_state.page = 'home'
        st.rerun()

elif st.session_state.page == 'summary_page':
    result_csv()
    if os.path.exists('fb.csv'):
        df = pd.read_csv('fb.csv')
        st.subheader('SUMMARY')
        st.write("total number of participants", len(df))
        try:
            st.write('please click here to see the table and the participants results')
            with st.expander('Results'):

                row=df[['q1', 'q2', 'q3', 'q4']]
                r=row.isin(['roti canai','nasi lemak','char kuey teow','satay']).astype(int)

                percentm = (df['Score']/ 4) * 100
                df['percentage'] = percentm
                st.dataframe(df)
                st.write('total mark of quiz')
                total_quiz_score=df['Score'].sum()
                st.write(f"total mark of quiz: {total_quiz_score}")

                st.write('___Score___')
                st.write(f'mean of the score {df['Score'].mean()}')
                st.write(f'median of the score {df['Score'].median()}')
                st.write(f'minimum of the score {df['Score'].min()}')
                st.write(f'maximum of the score {df['Score'].max()}')

                st.write('___Percentage___')
                st.write(f'mean of the percentage {df['percentage'].mean()}')
                st.write(f'median of the percentage {df['percentage'].median()}')
                st.write(f'minimum of the percentage {df['percentage'].min()}')
                st.write(f'maximum of the percentage {df['percentage'].max()}')

                st.write('marks get by students per question')
                st.write('total mark of question 1 : ', r['q1'].sum())
                st.write('total mark of question 2 : ', r['q2'].sum())
                st.write('total mark of question 3 : ', r['q3'].sum())
                st.write('total mark of question 4 : ', r['q4'].sum())

                st.bar_chart(df,x='Name',y='Score')
                df['mean_par']=r.mean(axis=1)
                st.bar_chart(df,x='Name',y='mean_par')
                df['med_par'] = r.median(axis=1)
                st.bar_chart(df,x='Name',y='med_par')
        except FileNotFoundError:
            st.warning('file not found')
    if st.button('Quit'):
        st.session_state.clear()
        st.session_state.page = 'home'
        st.rerun()



