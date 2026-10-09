import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Quản lý điểm sinh viên", page_icon="🎓", layout="wide")
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Dữ liệu mẫu 10 sinh viên; có thể thay bằng dữ liệu thật của lớp.
data = {
    "Ho_ten": ["An", "Bình", "Chi", "Dũng", "Hà", "Lan", "Minh", "Nam", "Phúc", "Trang"],
    "Chuyen_can": [8.0, 7.5, 9.0, 6.5, 8.5, 7.0, 9.5, 6.0, 8.0, 9.0],
    "Giua_ky":   [7.5, 8.0, 6.5, 7.0, 8.5, 6.0, 9.0, 7.5, 7.0, 8.0],
    "Cuoi_ky":   [8.5, 7.0, 7.5, 8.0, 9.0, 6.5, 8.5, 7.0, 7.5, 9.5],
}
df = pd.DataFrame(data)
df["Tong_ket"] = 0.2 * df["Chuyen_can"] + 0.3 * df["Giua_ky"] + 0.5 * df["Cuoi_ky"]

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)
df["Tong_ket"] = df["Tong_ket"].round(2)

st.subheader("Bảng điểm 10 sinh viên")
st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader("Thống kê lớp")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Điểm trung bình", f"{df['Tong_ket'].mean():.2f}")
c2.metric("Điểm cao nhất", f"{df['Tong_ket'].max():.2f}")
c3.metric("Điểm thấp nhất", f"{df['Tong_ket'].min():.2f}")
c4.metric("Số sinh viên đạt (≥ 5)", int((df["Tong_ket"] >= 5).sum()))

best = df.loc[df["Tong_ket"].idxmax()]
worst = df.loc[df["Tong_ket"].idxmin()]
st.write(f"**Điểm cao nhất:** {best['Ho_ten']} — {best['Tong_ket']:.2f}")
st.write(f"**Điểm thấp nhất:** {worst['Ho_ten']} — {worst['Tong_ket']:.2f}")

st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(df["Ho_ten"], df["Tong_ket"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Tên sinh viên")
ax.set_xlim(0, 10)
ax.grid(axis="x", linestyle="--", alpha=0.35)
st.pyplot(fig)
plt.close(fig)

st.subheader("Tra cứu điểm theo sinh viên")
ten = st.selectbox("Chọn sinh viên", df["Ho_ten"].tolist())
sv = df.loc[df["Ho_ten"] == ten].iloc[0]
a, b, c, d = st.columns(4)
a.metric("Chuyên cần", f"{sv['Chuyen_can']:.1f}")
b.metric("Giữa kỳ", f"{sv['Giua_ky']:.1f}")
c.metric("Cuối kỳ", f"{sv['Cuoi_ky']:.1f}")
d.metric("Tổng kết", f"{sv['Tong_ket']:.2f}")
st.info(f"Xếp loại: **{sv['Xep_loai']}**")

st.caption("Project thực hành Python — Quản lý điểm sinh viên.")
st.caption("Người thực hiện: [Điền họ tên] | MSSV: [Điền MSSV]")
