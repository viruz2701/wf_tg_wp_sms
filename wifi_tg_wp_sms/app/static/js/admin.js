document.addEventListener('DOMContentLoaded', function() {
    // Управление таблицами
    document.querySelectorAll('table').forEach(table => {
        new Tablesort(table);
    });

    // Удаление клиентов
    document.querySelectorAll('.btn-danger').forEach(btn => {
        btn.addEventListener('click', function(e) {
            if (!confirm('Вы уверены, что хотите удалить клиента?')) {
                e.preventDefault();
            }
        });
    });
});