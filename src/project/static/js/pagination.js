function arrangePageQuery(urlPath, pageToNavigate) {
    if (window.location.href.includes("?" )) {
        // there's filter queries in url:
        window.location.href = urlPath + "&page=" + pageToNavigate;
    } else {
        // there's no filter queries:
        window.location.href = urlPath + "?page=" + pageToNavigate;
    }
}

function navigateUrl(fullPath, pageToNavigate) {
    if (window.location.href.includes("?page=")) {
        // to avoid appending when there is no filter queries, remove page query:
        let baseFullPath = window.location.href.split("?page=")[0]
        window.location.href = baseFullPath + "?page=" + pageToNavigate;
        return
    }

    if (window.location.href.includes("&page=")) {
        // to avoid appending when there is filter queries, remove page query
        let baseFullPath = window.location.href.split("&page=")[0]
        arrangePageQuery(baseFullPath, pageToNavigate);
    } else {
        arrangePageQuery(fullPath, pageToNavigate)
    }
}
