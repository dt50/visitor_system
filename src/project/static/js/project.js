/* Project specific Javascript goes here. */

jQuery(document).ready(function ($) {
    $('[data-toggle="tooltip"], [class="tooltip_header"]').tooltip({
        "placement": "right"
    });

    const dropdownElementList = document.querySelectorAll('.dropdown-toggle');
    const dropdownList = [...dropdownElementList]
        .map(dropdownToggleEl => new bootstrap.Dropdown(dropdownToggleEl));

    let tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    let tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })
});
