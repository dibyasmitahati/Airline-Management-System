$(document).ready(function () {
    function loadRefunds() {
        $.ajax({
            url: '/get_refunds',
            method: 'GET',
            success: function (data) {
                const refundTable = $('#refundTableBody');
                refundTable.empty();
                data.forEach(refund => {
                    refundTable.append(`
                        <tr>
                            <td>${refund.refund_id}</td>
                            <td>${refund.user_id}</td>
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
            }
        });
    }

    window.clearRefund = function (refundId) {
        if (confirm('Are you sure you want to clear this refund?')) {
            $.post('/clear_refund', { refund_id: refundId }, function () {
                loadRefunds();
            });
        }
    };

    window.declineRefund = function (refundId) {
        if (confirm('Are you sure you want to decline this refund?')) {
            $.post('/decline_refund', { refund_id: refundId }, function () {
                loadRefunds();
            });
        }
    };

    window.reportFraud = function (refundId) {
        if (confirm('Are you sure you want to report this as fraud?')) {
            $.post('/report_fraud', { refund_id: refundId }, function () {
                loadRefunds();
            });
        }
    };

    loadRefunds();
});
