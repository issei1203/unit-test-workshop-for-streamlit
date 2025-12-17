import streamlit as st
import hashlib
import time

# === 運賃データ (結合ロジックの一部として機能) ===
# 運賃は片道あたりの価格 (大人料金)
FARES = {
    ("東京", "新宿"): 200,
    ("新宿", "東京"): 200,
    ("東京", "横浜"): 480,
    ("横浜", "東京"): 480,
    ("大阪", "京都"): 570,
    ("京都", "大阪"): 570,
}

STATIONS = sorted(list(set([s for pair in FARES.keys() for s in pair])))

def run_app():
    st.title("🎫 シンプルな電車の切符購入システム")
    st.markdown("---")


    col1, col2 = st.columns(2)

    with col1:
        departure = st.selectbox("1. 出発駅を選択", STATIONS, index=STATIONS.index("東京") if "東京" in STATIONS else 0)

    with col2:
        destination = st.selectbox("2. 到着駅を選択", STATIONS, index=STATIONS.index("新宿") if "新宿" in STATIONS else 0)

    trip_type = st.radio("3. 種別を選択", ["片道", "往復"])

    st.markdown("---")


    fare_key = (departure, destination)
    one_way_fare = FARES.get(fare_key)

    current_total = 0
    if one_way_fare is None:
        st.warning("選択された区間の運賃が見つかりません。")
        current_total = 0
    else:
        if trip_type == "片道":
            current_total = one_way_fare
        else: # 往復の場合
            current_total = one_way_fare + one_way_fare

    st.metric(
        label=f"{departure} → {destination} の合計運賃",
        value=f"¥ {current_total:,} 円"
    )

    # === 購入ボタンと購入処理ロジック ===

    if st.button("購入を確定する", use_container_width=True, type="primary"):
        if departure == destination:
            st.error("エラー: 出発駅と到着駅を別の駅にしてください。")
            return

        if one_way_fare is None:
            st.error("エラー: 選択された区間の運賃データが見つかりません。")
            return

        final_fare = 0
        if trip_type == "片道":
            final_fare = one_way_fare
        else:
            final_fare = one_way_fare + one_way_fare

        with st.spinner("決済処理中..."):
            time.sleep(1)

        # QRコードリンク生成ロジック
        # ユーザー選択内容と時刻をハッシュ化して一意なIDとする
        purchase_data = f"{departure}-{destination}-{trip_type}-{final_fare}-{time.time()}"
        ticket_id = hashlib.sha256(purchase_data.encode()).hexdigest()[:10]
        qr_code_link = f"https://example.com/ticket/{ticket_id}?type={trip_type}"

        # 成功メッセージと結果表示
        st.success("✅ 切符の購入が完了しました！")
        st.metric("お支払い額", f"¥ {final_fare:,} 円")

        st.subheader("📱 電子切符QRコード")
        st.markdown(
            f"以下のリンクからQRコードを表示し、改札機にかざしてください。"
        )
        st.code(qr_code_link)

# Streamlitの実行
if __name__ == "__main__":
    run_app()