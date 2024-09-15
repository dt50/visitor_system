json_i18n = `
    {
        "date": "Дата",
    }
`

js_i18n = JSON.parse(json_i18n);

function gettext(translate) {
    return js_i18n[translate] !== undefined ? js_i18n[translate] : translate
}
