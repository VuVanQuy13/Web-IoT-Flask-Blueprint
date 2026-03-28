// 1. Lấy ID từ URL một cách an toàn hơn
const pathParts = window.location.pathname.split('/').filter(p => p !== "");
const gId = pathParts[pathParts.length - 1];

// 2. Đưa loadTab ra ngoài hoặc gán vào window để file con (number_mush.js) gọi được
async function loadTab(e, type) {
    if (e) {
        e.preventDefault();
        // Xóa active cũ
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        e.currentTarget.classList.add('active');
    }

    const container = document.getElementById('display-content');

    // Loading UI
    container.innerHTML = `
        <div class="text-center py-5">
            <div class="spinner-grow text-success" role="status"></div>
            <p class="text-muted mt-2">Đang kết nối trạm dữ liệu vườn #${gId}...</p>
        </div>`;

    const routes = {
        'sensor': `/mushroom/api/sensor/${gId}`,
        'quantity': `/mushroom/api/quantity/${gId}`,
        'schedule': `/mushroom/api/schedule/${gId}`
    };

    try {
        const res = await fetch(routes[type]);
        if (!res.ok) throw new Error("Server không phản hồi (404/500)");

        const html = await res.text();
        container.innerHTML = html;

        // 3. Khởi tạo JS cho nội dung vừa mới load xong
        initFeatureJS(type);

    } catch (err) {
        container.innerHTML = `
            <div class="alert alert-danger shadow-sm border-0 m-3">
                <i class="bi bi-exclamation-triangle-fill"></i> Lỗi: ${err.message}
            </div>`;
    }
}

// HÀM KHỞI TẠO JS THEO TAB (Đảm bảo các file .js con đã được load ở mushroom.html)
function initFeatureJS(type) {
    // console.log("Initializing JS for:", type); // Debug xem tab đã init chưa

    if (type === 'schedule' && typeof initWashCal === "function") {
        initWashCal();
    }

    if (type === 'sensor' && typeof initDataEnv === "function") {
        initDataEnv();
    }

    if (type === 'quantity' && typeof initNumMush === "function") {
        initNumMush();
    }
}

// Load mặc định tab đầu khi trang web sẵn sàng
document.addEventListener('DOMContentLoaded', () => {
    // Nếu bạn muốn tab mặc định là 'sensor'
    loadTab(null, 'sensor');
});

// Gán loadTab vào đối tượng window để các file JS khác gọi được (quan trọng cho Render lại)
window.loadTab = loadTab;