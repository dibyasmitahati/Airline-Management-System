$(document).ready(function () {
    function loadRefunds() {
        $.ajax({
            url: '/admin/get-refunds',  // Corrected URL
            method: 'GET',
            success: function (data) {
                const refundTable = $('#refundTableBody');
                refundTable.empty();
                data.forEach(refund => {
                    refundTable.append(`
                        <tr>
                            <td>${refund.refund_id}</td>
                            <td>${refund.ticket_id}</td>
                            <td>${refund.status}</td>
                            <td>
                                <button class="action-btn btn-clear" onclick="clearRefund(${refund.refund_id})">Clear</button>
                                <button class="action-btn btn-decline" onclick="declineRefund(${refund.refund_id})">Decline</button>
                                <button class="action-btn btn-fraud" onclick="reportFraud(${refund.refund_id})">Report Fraud</button>
                            </td>
                        </tr>
                    `);
                });
            },
            error: function (xhr, status, error) {
                console.error("Error fetching refunds:", error);
            }
        });
    }

    window.clearRefund = function (refundId) {
        if (confirm('Are you sure you want to clear this refund?')) {
            $.post('/admin/clear-refund', { refund_id: refundId }, function () {
                loadRefunds();
            });
        }
    };

    window.declineRefund = function (refundId) {
        if (confirm('Are you sure you want to decline this refund?')) {
            $.post('/admin/decline-refund', { refund_id: refundId }, function () {
                loadRefunds();
            });
        }
    };

    window.reportFraud = function (refundId) {
        if (confirm('Are you sure you want to report this as fraud?')) {
            $.post('/admin/report-fraud', { refund_id: refundId }, function () {
                loadRefunds();
            });
        }
    };

    loadRefunds();
});