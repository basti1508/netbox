import { getElements, isTruthy } from './util';
import { initButtons } from './buttons';
import { initSelect } from './select';

function initDepedencies(): void {
  console.log('initDepedencies()');
  for (const init of [initButtons, initSelect]) {
    init();
  }
}

/**
 * Hook into HTMX's event system to reinitialize specific native event listeners when HTMX swaps
 * elements.
 */
export function initHtmx(): void {
  for (const element of getElements('[hx-target]')) {
    const targetSelector = element.getAttribute('hx-target');
    if (isTruthy(targetSelector)) {
      for (const target of getElements(targetSelector)) {
        target.addEventListener('htmx:afterSettle', initDepedencies);
      }
    }
  }
}
