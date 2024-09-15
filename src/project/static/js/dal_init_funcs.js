if ((_element = jQuery("select[data-autocomplete-light-function]").not("[data-autocomplete-light-function*=select2]")).length > 0) {
    _element.each(function () {
        const func = $(this).attr("data-autocomplete-light-function");

        gauntface.logger.log("Initializing a function " + func)

        $(document).on('dal-init-function', function () {
            yl.registerFunction(func, function ($, element) {
                let $element = $(element);

                $element.select2({
                    ajax: {
                        url: $element.data("autocomplete-light-url"),
                        delay: 150
                    },
                    placeholder: $element.attr("placeholder")
                });
            });
        });
    })
} else {
    gauntface.logger.info("No custom DAL functions");
}
