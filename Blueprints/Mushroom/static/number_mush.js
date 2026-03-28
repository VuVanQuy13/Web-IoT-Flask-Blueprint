function initNumMush() {
    // 1. Lấy ID vườn từ URL
    const pathParts = window.location.pathname.split('/').filter(p => p !== "");
    const currentId = pathParts[pathParts.length - 1];

    const btnAdd = document.getElementById("btn-add");

    // 2. XỬ LÝ THÊM MỚI
    if (btnAdd) {
        btnAdd.onclick = async function (e) {
            e.preventDefault();

            const tenNam = document.getElementById("ten-nam").value.trim();
            const date = document.getElementById("ngay-trong").value;
            // Lấy thêm giá trị thời gian sinh trưởng
            const tgSinhTruong = document.getElementById("tg-sinh-truong").value;

            if (!tenNam || !date || !tgSinhTruong) {
                alert("Vui lòng nhập đầy đủ: Tên nấm, Ngày trồng và Chu kỳ sinh trưởng!");
                return;
            }

            try {
                const res = await fetch(`/mushroom/api/add_mushroom/${currentId}`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ 
                        ten_nam: tenNam, 
                        date: date,
                        tg_sinh_truong: parseInt(tgSinhTruong) // Gửi thêm trường này
                    })
                });

                const data = await res.json();

                if (data.status === "success") {
                    // Render lại tab để cập nhật bảng
                    if (typeof loadTab === "function") {
                        loadTab(null, "quantity");
                    }
                } else {
                    alert("Lỗi server: " + data.message);
                }
            } catch (err) {
                console.error("Fetch error:", err);
                alert("Không kết nối được server!");
            }
        };
    }

    // 3. XỬ LÝ THU HOẠCH
    const harvestButtons = document.querySelectorAll(".btn-harvest");
    harvestButtons.forEach(btn => {
        btn.onclick = async function (e) {
            e.preventDefault();
            
            const id = this.getAttribute("data-id");
            const kg = prompt("Nhập sản lượng thu hoạch (kg):");

            if (kg === null) return; 
            if (kg.trim() === "" || isNaN(kg) || parseFloat(kg) <= 0) {
                alert("Vui lòng nhập số lượng kg hợp lệ!");
                return;
            }

            try {
                const res = await fetch(`/mushroom/api/harvest/${id}`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ kg: kg })
                });
                
                const data = await res.json();
                
                if (data.status === "success") {
                    loadTab(null, "quantity");
                } else {
                    alert("Lỗi: " + data.message);
                }
            } catch (err) {
                console.error("Harvest error:", err);
                alert("Lỗi kết nối khi thu hoạch!");
            }
        };
    });
}