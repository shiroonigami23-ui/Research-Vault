# Evidence and Validation Notes

## What Existing Literature Supports

1. Prompt-only alignment is not equivalent to hard enforcement.
2. Indirect prompt injection is a real systems problem, not only a toy prompt problem.
3. Jailbreak attacks can be automated and transferred.
4. External control layers are more defensible than language-only rules.

## What We Still Need to Prove

1. a formal linguistic smart contract architecture can outperform prompt-only safety,
2. contract triggers can be specified with low ambiguity,
3. enforcement can remain robust under paraphrase, attack, and tool-use pressure,
4. strict policies do not destroy too much useful capability.

## Validation Path

- define a minimal policy language,
- compile it into machine checks,
- evaluate against a jailbreak/prompt injection benchmark,
- compare prompt-only, classifier-gated, and contract-enforced systems.
