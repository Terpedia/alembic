(function () {
  'use strict';

  const promptInput = document.getElementById('prompt-input');
  const outputPanel = document.getElementById('output-panel');
  const apiPanel = document.getElementById('api-panel');
  const commandCode = document.getElementById('command-code');
  const btnGetCommand = document.getElementById('btn-get-command');
  const btnReportPreset = document.getElementById('btn-report-preset');

  function escapeShellArg(s) {
    if (!s || !s.trim()) return '""';
    const t = s.trim().replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/\n/g, ' ');
    return '"' + t + '"';
  }

  function buildCommand(prompt) {
    const arg = escapeShellArg(prompt);
    return 'python -m alembic ' + arg;
  }

  function showCommand(prompt) {
    if (!prompt || !prompt.trim()) {
      promptInput.placeholder = 'Enter a question or report topic first.';
      promptInput.focus();
      return;
    }
    const cmd = buildCommand(prompt.trim());
    commandCode.textContent = cmd;
    outputPanel.classList.remove('hidden');
    apiPanel.classList.add('hidden');
  }

  function copySnippet(elementId) {
    const el = document.getElementById(elementId);
    if (!el) return;
    const code = el.querySelector('code') || el;
    const text = code.textContent || '';
    navigator.clipboard.writeText(text).then(
      function () {
        const btn = document.querySelector('[data-copy-target="' + elementId + '"]');
        if (btn) {
          const orig = btn.textContent;
          btn.textContent = 'Copied!';
          setTimeout(function () {
            btn.textContent = orig;
          }, 1500);
        }
      },
      function () {
        var range = document.createRange();
        range.selectNodeContents(code);
        document.getSelection().removeAllRanges();
        document.getSelection().addRange(range);
      }
    );
  }

  function reportPreset() {
    promptInput.value = 'Write a concise, well-structured report (with short sections and bullet points where useful) on the following topic. Use clear headings and keep each section to a few paragraphs.';
    promptInput.placeholder = 'Add your topic here, e.g. "terpenes and entourage effect" or "CBD and anxiety: current evidence".';
    promptInput.focus();
  }

  document.body.addEventListener('click', function (e) {
    var btn = e.target.closest('.copy-btn');
    if (!btn || !btn.dataset.copyTarget) return;
    e.preventDefault();
    copySnippet(btn.dataset.copyTarget);
  });

  btnGetCommand.addEventListener('click', function () {
    showCommand(promptInput.value);
  });

  btnReportPreset.addEventListener('click', reportPreset);

  promptInput.addEventListener('keydown', function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      e.preventDefault();
      showCommand(promptInput.value);
    }
  });
})();
