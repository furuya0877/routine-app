import streamlit as st
from datetime import datetime, timedelta

st.title("🛏️ 起床・就寝時間アプリ")

# タスク選択
task_options = {
    "朝ジョギング＋風呂（60分）": 60,
    "朝ジョギング（汗かかない程度）（35分）": 35,
    "通常の準備（25分）": 25
}

selected_tasks = st.multiselect("やることを選んでください", options=list(task_options.keys()))

# 出発時間の選択（時・分）
col1, col2 = st.columns(2)
with col1:
    hour = st.selectbox("出発：時", list(range(0, 24)), index=8)
with col2:
    minute = st.selectbox("出発：分", list(range(0, 60, 10)), index=0)

# 睡眠時間スライダー
sleep_hours = st.slider("睡眠時間（時間）", 6.0, 9.0, 7.5, 0.5)

# 計算実行ボタン
if st.button("起床・就寝時間を計算"):
    if not selected_tasks:
        st.warning("最低1つは選んでください！")
    else:
        total_minutes = sum([task_options[task] for task in selected_tasks])
        departure_time = datetime.strptime(f"{hour}:{minute:02d}", "%H:%M")
        wake_time = departure_time - timedelta(minutes=total_minutes)
        sleep_time = wake_time - timedelta(hours=sleep_hours)

        st.markdown("### ✅ 結果")
        st.write("📝 選んだタスク:")
        for t in selected_tasks:
            st.write(f"・{t}")
        st.write(f"🏃 出発時間: {departure_time.strftime('%H:%M')}")
        st.write(f"🕒 起床時間: {wake_time.strftime('%H:%M')}")
        st.write(f"💤 就寝時間: {sleep_time.strftime('%H:%M')}（睡眠 {sleep_hours:.1f} 時間）")
