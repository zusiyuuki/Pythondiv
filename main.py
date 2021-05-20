
import streamlit as st
import time
st.title('Streamlit 超入門')
st.write('プログレスバーの表示')
'Start!!'
latest_iterataon=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iterataon.text(f'iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!!'

st.write('Interactive Widgets')
left_column,right_column =st.beta_columns(2)

button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を表示')

# text =st.text_input('あなたの趣味を教えてください。')
# condistion=st.slider('あなたの今の調子はどうですか？',0,100,50)

# 'あなたの趣味は,',text,'です。'
# 'コンディション:',condistion,'です'

