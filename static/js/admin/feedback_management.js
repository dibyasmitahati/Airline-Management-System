$(document).ready(function () {
    function loadFeedback() {
        $.ajax({
            url: '/admin/get-feedback',
            method: 'GET',
            success: function (data) {
                if (data.error) {
                    $('#feedbackTable').html(`<tr><td colspan="7" class="text-center">${data.error}</td></tr>`);
                    return;
                }

                let feedbackHtml = '';
                data.forEach((feedback, index) => {
                    feedbackHtml += `
                        <tr>
                            <td>${index + 1}</td>
                            <td>${feedback.message}</td>
                            <td>${feedback.message_of_review}</td>
                            <td>${feedback.message_email}</td>
                            <td>${feedback.message_author}</td>
                            <td>${feedback.author_country}</td>
                            <td>
                                <button class="btn btn-danger btn-sm delete-feedback" data-id="${feedback.message_id}">
                                    <i class="fa fa-trash"></i> Delete
                                </button>
                            </td>
                        </tr>
                    `;
                });
                $('#feedbackTable').html(feedbackHtml);
            },
            error: function () {
                alert('Failed to fetch feedback. Please try again.');
            },
        });
    }

    $(document).on('click', '.delete-feedback', function () {
        const messageId = $(this).data('id');
        if (confirm('Are you sure you want to delete this feedback?')) {
            $.ajax({
                url: `/admin/delete-feedback/${messageId}`,
                method: 'POST',
                success: function (response) {
                    if (response.error) {
                        alert('Error: ' + response.error);
                    } else {
                        alert(response.message);
                        loadFeedback();
                    }
                },
                error: function (xhr) {
                    if (xhr.status === 404) {
                        alert('Error: Feedback not found.');
                    } else {
                        alert('Failed to delete feedback. Please try again.');
                    }
                },
            });
        }
    });

    loadFeedback();
});
