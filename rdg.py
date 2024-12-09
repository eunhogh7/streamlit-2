import streamlit as st

# 앱 제목
st.title("비빔밥 레시피 커스터마이징 앱 🍚")

# 비빔밥 기본 재료 선택
st.header("1. 기본 재료 선택")
rice = st.radio("밥 종류를 선택하세요:", ("흰쌀밥", "현미밥", "잡곡밥"))

# 나물 및 추가 재료
st.header("2. 나물 및 추가 재료 선택")
veggies = st.multiselect(
    "좋아하는 나물을 선택하세요:",
    ["시금치", "도라지", "고사리", "콩나물", "무나물", "호박나물"]
)
proteins = st.multiselect(
    "단백질 추가하기:",
    ["불고기", "계란 프라이", "두부", "닭가슴살"]
)
sauce = st.radio("소스 선택:", ("고추장", "간장", "참기름"))

# 추가 토핑
st.header("3. 추가 토핑 선택")
toppings = st.multiselect(
    "원하는 추가 토핑:",
    ["깨", "김가루", "양념장", "김치", "아보카도"]
)

# 최종 레시피 표시
st.header("4. 나만의 비빔밥 레시피 🍴")
if st.button("레시피 확인"):
    st.subheader("📋 선택한 재료:")
    st.write(f"밥: {rice}")
    st.write(f"나물: {', '.join(veggies) if veggies else '선택하지 않음'}")
    st.write(f"단백질: {', '.join(proteins) if proteins else '선택하지 않음'}")
    st.write(f"소스: {sauce}")
    st.write(f"추가 토핑: {', '.join(toppings) if toppings else '선택하지 않음'}")
    st.success("맛있게 드세요! 😋")

# 푸터
st.text("만든 이: 당신의 비빔밥 도우미")
