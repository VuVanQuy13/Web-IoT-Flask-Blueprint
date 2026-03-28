function initWashCal() {
    const btnSave = document.getElementById('btn-save-wash');
    const timeInput = document.getElementById('schedule-time');

    let editId = null;

    // ===== THÊM / CẬP NHẬT =====
    if (btnSave) {
        btnSave.onclick = async function () {
            const gardenId = this.getAttribute('data-id');
            const timeValue = timeInput.value;

            if (!timeValue) {
                alert("Vui lòng chọn thời gian!");
                return;
            }

            const formattedTime = timeValue.replace('T', ' ');

            let url = `/mushroom/api/add_schedule/${gardenId}`;
            let method = "POST";

            // Nếu đang sửa
            if (editId) {
                url = `/mushroom/api/update_schedule/${editId}`;
                method = "PUT";
            }

            const res = await fetch(url, {
                method: method,
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ time: formattedTime })
            });

            const data = await res.json();

            if (data.status === "success") {
                editId = null;
                btnSave.innerHTML = `<i class="bi bi-save"></i> LƯU LỊCH TƯỚI`;
                timeInput.value = "";
                loadTab(null, 'schedule');
            } else {
                alert(data.message);
            }
        };
    }

    // ===== CLICK SỬA =====
    document.querySelectorAll('.btn-edit').forEach(btn => {
        btn.onclick = function () {
            const id = this.getAttribute('data-id');
            const time = this.getAttribute('data-time');

            editId = id;

            // Convert sang format datetime-local
            const formatted = time.replace(' ', 'T');
            timeInput.value = formatted;

            btnSave.innerHTML = `<i class="bi bi-pencil"></i> CẬP NHẬT`;
        };
    });

    // ===== XÓA =====
    document.querySelectorAll('.btn-delete').forEach(btn => {
        btn.onclick = async function () {
            const id = this.getAttribute('data-id');

            if (!confirm("Bạn có chắc muốn xóa?")) return;

            const res = await fetch(`/mushroom/api/delete_schedule/${id}`, {
                method: 'DELETE'
            });

            const data = await res.json();

            if (data.status === "success") {
                loadTab(null, 'schedule');
            } else {
                alert(data.message);
            }
        };
    });
}