<script>
    document.addEventListener('DOMContentLoaded', function () {
        const dropdown = document.querySelector('.dropdown');
        const dropdownLink = dropdown.parentElement.querySelector('a');

        dropdownLink.addEventListener('click', function (e) {
            e.preventDefault();
            dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
        });
    });
</script>
