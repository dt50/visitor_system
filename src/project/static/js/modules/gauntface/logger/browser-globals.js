var __defProp = Object.defineProperty;
var __export = (target, all) => {
    for (var name in all)
        __defProp(target, name, {get: all[name], enumerable: true});
};

// src/browser/browser.js
var browser_exports = {};
__export(browser_exports, {
    LogLevels: () => LogLevels_exports,
    Logger: () => BrowserLogger,
    logger: () => logger
});

// src/types/_LogLevels.js
var LogLevels_exports = {};
__export(LogLevels_exports, {
    DEBUG: () => DEBUG,
    ERROR: () => ERROR,
    GROUP: () => GROUP,
    INFO: () => INFO,
    LOG: () => LOG,
    SILENCE: () => SILENCE,
    WARN: () => WARN
});
var DEBUG = 0;
var INFO = 1;
var LOG = 2;
var WARN = 3;
var ERROR = 4;
var GROUP = 5;
var SILENCE = 6;

// src/shared/_AbstractLogger.js
var DEFAULT_PREFIXES = {
    [DEBUG]: "\u{1F41B}",
    [INFO]: "\u2139\uFE0F",
    [LOG]: "\u{1F4AC}",
    [WARN]: "\u26A0\uFE0F",
    [ERROR]: "\u2620\uFE0F",
    [GROUP]: "\u{1F9F5}"
};
var AbstractLogger = class {
    constructor(opts) {
        this.opts = opts || {};
        this.setPrefix(this.opts.prefix);
        this.currentLogLevel = this.getDefaultLogLevel();
    }

    setPrefix(prefix) {
        if (!prefix) {
            this.opts.prefix = DEFAULT_PREFIXES;
        } else if (typeof prefix == "object") {
            this.opts.prefix = {};
            for (const k of Object.keys(DEFAULT_PREFIXES)) {
                this.opts.prefix[k] = prefix[k] || DEFAULT_PREFIXES[k];
            }
        } else {
            this.opts.prefix = prefix;
        }
    }

    setLogLevel(logLevel) {
        this.currentLogLevel = logLevel;
    }

    debug(...args) {
        this.print(console.debug, DEBUG, args);
    }

    info(...args) {
        this.print(console.info, INFO, args);
    }

    log(...args) {
        this.print(console.log, LOG, args);
    }

    warn(...args) {
        this.print(console.warn, WARN, args);
    }

    error(...args) {
        this.print(console.error, ERROR, args);
    }

    group(...args) {
        this.print(console.group, GROUP, args);
    }

    groupCollapsed(...args) {
        this.print(console.groupCollapsed, GROUP, args);
    }

    groupEnd() {
        console.groupEnd();
    }

    print(consoleFunc, logLevel, args) {
        if (this.currentLogLevel > logLevel) {
            return;
        }
        consoleFunc(...this.getArgs(logLevel, args));
    }

    getArgs(logLevel, args) {
        const prefix = this.getPrefix(logLevel);
        if (prefix) {
            return [...prefix, ...args];
        }
        return args;
    }

    getPrefix(logLevel) {
        let pre = this.opts.prefix;
        if (!pre) {
            pre = DEFAULT_PREFIXES;
        }
        let s = pre;
        if (typeof s == "object") {
            s = pre[logLevel];
        }
        return this.colorPrefix(logLevel, s);
    }

    getDefaultLogLevel() {
        return DEBUG;
    }
};

// src/types/_LogColors.js
var DEBUG2 = {
    red: 99,
    green: 110,
    blue: 114
};
var INFO2 = {
    red: 72,
    green: 126,
    blue: 176
};
var LOG2 = {
    red: 76,
    green: 209,
    blue: 55
};
var WARN2 = {
    red: 225,
    green: 177,
    blue: 44
};
var ERROR2 = {
    red: 231,
    green: 76,
    blue: 60
};
var GROUP2 = {
    red: 0,
    green: 168,
    blue: 255
};

// src/browser/_BrowserLogger.js
var BrowserLogger = class extends AbstractLogger {
    colorPrefix(logLevel, prefix) {
        return [`%c${prefix}`, this.getLevelCSS(logLevel)];
    }

    getLevelCSS(logLevel) {
        function getStyles(color) {
            return `background: rgb(${color.red}, ${color.green}, ${color.blue}); color: white; padding: 2px 0.5em; border-radius: 0.5em`;
        }

        switch (logLevel) {
            case DEBUG:
                return getStyles(DEBUG2);
            case INFO:
                return getStyles(INFO2);
            case WARN:
                return getStyles(WARN2);
            case ERROR:
                return getStyles(ERROR2);
            case GROUP:
                return getStyles(GROUP2);
            case LOG:
            default:
                return getStyles(LOG2);
        }
    }
};

// src/browser/browser.js
var logger = new BrowserLogger();

// src/browser/browser-globals.js
window["gauntface"] = window["gauntface"] || {};
Object.assign(window["gauntface"], browser_exports);
//# sourceMappingURL=browser-globals.js.map
