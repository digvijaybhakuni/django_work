/**
 * @license
 * Copyright 2015 Google Inc. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

(function () {
    'use strict';

    /**
     * Class constructor for Datefield MDL component.
     * Implements MDL component design pattern defined at:
     * https://github.com/jasonmayes/mdl-component-design-pattern
     *
     * @constructor
     * @param {HTMLElement} element The element that will be upgraded.
     */
    var MaterialDatefield = function MaterialDatefield(element) {
        this.element_ = element;
        this.maxRows = this.Constant_.NO_MAX_ROWS;
        // Initialize instance.
        this.init();
    };
    window['MaterialDatefield'] = MaterialDatefield;

    /**
     * Store constants in one place so they can be updated easily.
     *
     * @enum {string | number}
     * @private
     */
    MaterialDatefield.prototype.Constant_ = {
        NO_MAX_ROWS: -1
        , MAX_ROWS_ATTRIBUTE: 'maxrows'
    };

    /**
     * Store strings for class names defined by this component that are used in
     * JavaScript. This allows us to simply change it in one place should we
     * decide to modify at a later date.
     *
     * @enum {string}
     * @private
     */
    MaterialDatefield.prototype.CssClasses_ = {
        LABEL: 'mdl-datefield__label'
        , INPUT: 'mdl-datefield__date'
        , IS_DIRTY: 'is-dirty'
        , IS_FOCUSED: 'is-focused'
        , IS_DISABLED: 'is-disabled'
        , IS_INVALID: 'is-invalid'
        , IS_UPGRADED: 'is-upgraded'
        , HAS_PLACEHOLDER: 'has-placeholder'
        , DATE_DIALOG: 'mdl-dialog'
        , DATE_DIALOG_TITLE: 'mdl-dialog__title'
    };

    /**
     * Handle date being entered.
     *
     * @param {Event} event The event that fired.
     * @private
     */
    MaterialDatefield.prototype.onKeyDown_ = function (event) {
        var currentRowCount = event.target.value.split('\n').length;
        if (event.keyCode === 13) {
            if (currentRowCount >= this.maxRows) {
                event.preventDefault();
            }
        }
    };

    /**
     * Handle focus.
     *
     * @param {Event} event The event that fired.
     * @private
     */
    MaterialDatefield.prototype.onFocus_ = function (event) {
        this.element_.classList.add(this.CssClasses_.IS_FOCUSED);
    };

    /**
     * Handle lost focus.
     *
     * @param {Event} event The event that fired.
     * @private
     */
    MaterialDatefield.prototype.onBlur_ = function (event) {
        this.element_.classList.remove(this.CssClasses_.IS_FOCUSED);
    };

    /**
     * Handle reset event from out side.
     *
     * @param {Event} event The event that fired.
     * @private
     */
    MaterialDatefield.prototype.onReset_ = function (event) {
        this.updateClasses_();
    };

    /**
     * Handle class updates.
     *
     * @private
     */
    MaterialDatefield.prototype.updateClasses_ = function () {
        this.checkDisabled();
        this.checkValidity();
        this.checkDirty();
        this.checkFocus();
    };

    // Public methods.

    /**
     * Check the disabled state and update field accordingly.
     *
     * @public
     */
    MaterialDatefield.prototype.checkDisabled = function () {
        if (this.date_.disabled) {
            this.element_.classList.add(this.CssClasses_.IS_DISABLED);
        } else {
            this.element_.classList.remove(this.CssClasses_.IS_DISABLED);
        }
    };
    MaterialDatefield.prototype['checkDisabled'] =
        MaterialDatefield.prototype.checkDisabled;

    /**
     * Check the focus state and update field accordingly.
     *
     * @public
     */
    MaterialDatefield.prototype.checkFocus = function () {
        if (Boolean(this.element_.querySelector(':focus'))) {
            this.element_.classList.add(this.CssClasses_.IS_FOCUSED);
        } else {
            this.element_.classList.remove(this.CssClasses_.IS_FOCUSED);
        }
    };
    MaterialDatefield.prototype['checkFocus'] =
        MaterialDatefield.prototype.checkFocus;

    /**
     * Check the validity state and update field accordingly.
     *
     * @public
     */
    MaterialDatefield.prototype.checkValidity = function () {
        if (this.date_.validity) {
            if (this.date_.validity.valid) {
                this.element_.classList.remove(this.CssClasses_.IS_INVALID);
            } else {
                this.element_.classList.add(this.CssClasses_.IS_INVALID);
            }
        }
    };
    MaterialDatefield.prototype['checkValidity'] =
        MaterialDatefield.prototype.checkValidity;

    /**
     * Check the dirty state and update field accordingly.
     *
     * @public
     */
    MaterialDatefield.prototype.checkDirty = function () {
        if (this.date_.value && this.date_.value.length > 0) {
            this.element_.classList.add(this.CssClasses_.IS_DIRTY);
        } else {
            this.element_.classList.remove(this.CssClasses_.IS_DIRTY);
        }
    };
    MaterialDatefield.prototype['checkDirty'] =
        MaterialDatefield.prototype.checkDirty;

    /**
     * Disable text field.
     *
     * @public
     */
    MaterialDatefield.prototype.disable = function () {
        this.date_.disabled = true;
        this.updateClasses_();
    };
    MaterialDatefield.prototype['disable'] = MaterialDatefield.prototype.disable;

    /**
     * Enable text field.
     *
     * @public
     */
    MaterialDatefield.prototype.enable = function () {
        this.date_.disabled = false;
        this.updateClasses_();
    };
    MaterialDatefield.prototype['enable'] = MaterialDatefield.prototype.enable;

    /**
     * Update text field value.
     *
     * @param {string} value The value to which to set the control (optional).
     * @public
     */
    MaterialDatefield.prototype.change = function (value) {

        this.date_.value = value || '';
        this.updateClasses_();
    };
    MaterialDatefield.prototype['change'] = MaterialDatefield.prototype.change;


    MaterialDatefield.prototype.onClick_ = function (e) {

        //this.date_.value = value || "";

        var dateDialog = this.element_.querySelector('.' + this.CssClasses_.DATE_DIALOG);

        if (!dateDialog.showModal) {
            dialogPolyfill.registerDialog(dateDialog);
        }
        dateDialog.showModal();
        this.updateClasses_();
    }

    //MaterialDatefield.prototype['click'] = MaterialDatefield.prototype.onClick;


    MaterialDatefield.prototype.createDateDialog_ = function (date) {
        var _curDate = date || new Date();

        var _contentClob = '<h4 class="mdl-dialog__title">' + moment(_curDate).format('Do MMMM YYYY') + '</h4>'
            + '<div class="mdl-dialog__content">'
            + '<p>Test Content</p>'
            + '</div>'
            + '<div class="mdl-dialog__actions mdl-dialog__actions">'
            + '<button type="button" class="mdl-button">Close</button>'
            + '<button type="button" class="mdl-button" disabled>Inactive action</button>'
            + '</div>';

        return _contentClob;

    };

    /**
     * Initialize element.
     */
    MaterialDatefield.prototype.init = function () {

        if (this.element_) {
            this.label_ = this.element_.querySelector('.' + this.CssClasses_.LABEL);
            this.date_ = this.element_.querySelector('.' + this.CssClasses_.INPUT);

            var datePicker = document.createElement('dialog');
            //var dateSelected = document.createElement('h4');
            datePicker.innerHTML = this.createDateDialog_(new Date());
            //datePicker.appendChild(dateSelected);
            //datePicker.textContent = moment().format('MMM Do YY');

            datePicker.classList.add(this.CssClasses_.DATE_DIALOG);
            //dateSelected.classList.add(this.CssClasses_.DATE_DIALOG_TITLE);

            this.element_.appendChild(datePicker);

            if (this.date_) {
                if (this.date_.hasAttribute(
                        /** @type {string} */
                        (this.Constant_.MAX_ROWS_ATTRIBUTE))) {
                    this.maxRows = parseInt(this.date_.getAttribute(
                        /** @type {string} */
                        (this.Constant_.MAX_ROWS_ATTRIBUTE)), 10);
                    if (isNaN(this.maxRows)) {
                        this.maxRows = this.Constant_.NO_MAX_ROWS;
                    }
                }

                if (this.date_.hasAttribute('placeholder')) {
                    this.element_.classList.add(this.CssClasses_.HAS_PLACEHOLDER);
                }

                this.boundUpdateClassesHandler = this.updateClasses_.bind(this);
                this.boundFocusHandler = this.onFocus_.bind(this);
                this.boundBlurHandler = this.onBlur_.bind(this);
                this.boundResetHandler = this.onReset_.bind(this);
                this.boundItemClick_Date = this.onClick_.bind(this);
                this.date_.addEventListener('click', this.boundItemClick_Date);
                this.date_.addEventListener('input', this.boundUpdateClassesHandler);
                this.date_.addEventListener('focus', this.boundFocusHandler);
                this.date_.addEventListener('blur', this.boundBlurHandler);
                this.date_.addEventListener('reset', this.boundResetHandler);

                if (this.maxRows !== this.Constant_.NO_MAX_ROWS) {
                    // TODO: This should handle pasting multi line text.
                    // Currently doesn't.
                    this.boundKeyDownHandler = this.onKeyDown_.bind(this);
                    this.date_.addEventListener('keydown', this.boundKeyDownHandler);
                }
                var invalid = this.element_.classList
                    .contains(this.CssClasses_.IS_INVALID);
                this.updateClasses_();
                this.element_.classList.add(this.CssClasses_.IS_UPGRADED);
                if (invalid) {
                    this.element_.classList.add(this.CssClasses_.IS_INVALID);
                }
                if (this.date_.hasAttribute('autofocus')) {
                    this.element_.focus();
                    this.checkFocus();
                }
            }
        }
    };

    // The component registers itself. It can assume componentHandler is available
    // in the global scope.
    componentHandler.register({
        constructor: MaterialDatefield
        , classAsString: 'MaterialDatefield'
        , cssClass: 'mdl-js-datefield'
        , widget: true
    });
})();