import streamlit as st

st.title("学生 邵静雯-数字档案🥐🥐🥐")
st.header("基础信息")
st.subheader("学生ID：09")
st.subheader("学生性别：女🙋‍♀️")

st.image("http://pic.imeitou.com/uploads/allimg/241119/3-241119110225-50.jpg")
st.markdown("**:blue[注册时间：2025年10月20日10:57:23]**")
st.markdown("**:green[当前教室：实204]**")

st.header("技能矩阵😉😉😉")

import streamlit as st  # 导入Streamlit并用st代表它

st.subheader('技能')
# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="C语言", value="5%", delta="5%")
c2.metric(label="Python", value="56%", delta="6%")
c3.metric(label="Java", value=None, delta="0", delta_color="off")

st.subheader('收入情况')
st.metric(label="当日收入", value="300", delta="100")

st.header("任务日志📔📔📔")
import pandas as pd   # 导入Pandas并用pd代替
import streamlit as st  # 导入Streamlit并用st代表它

# 定义数据,以便创建数据框
data = {
    '日期':['2025-10-1','2025-10-2','2025-10-3'],
    '任务':['观看综艺','铲屎官职责','睡大觉'],
    '状态':['✔已完成','❌未完成','✔已完成'],
    '难度':['⭐⭐','⭐⭐⭐⭐','⭐'],
}
# 定义数据框所用的索引
index = pd.Series(['01', '02', '03'], name='任务')
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)

st.subheader('静态表')
st.table(df)

st.header("最新代码成果🤏🤏🤏")

str ='''
a=1000
b=314
print(a+b)
'''
st.code(str,language="python",line_numbers=True)
'------------------------------------------------'
st.markdown("#### **现状态：混乱中**")
st.markdown(':green[>>>SYSTEH MESSAGE:]下一个任务目标')
st.markdown(':green[>>>TARGET:]课程管理系统')
st.markdown(':green[>>>COUNTDOWN:]2025年10月20日11:55:54')
st.markdown("#### **连接状态：已加密**")





