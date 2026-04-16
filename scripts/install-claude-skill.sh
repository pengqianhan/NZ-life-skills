#!/usr/bin/env bash
set -euo pipefail

if [ "${1:-}" = "" ]; then
  echo "Usage: $0 <skill-name>"
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
SKILL_NAME="$1"
SOURCE_DIR="${REPO_DIR}/skills/${SKILL_NAME}"
TARGET_ROOT="${HOME}/.claude/skills"
TARGET_DIR="${TARGET_ROOT}/${SKILL_NAME}"

if [ ! -d "${SOURCE_DIR}" ]; then
  echo "Skill not found: ${SKILL_NAME}"
  exit 1
fi

mkdir -p "${TARGET_ROOT}"
rm -rf "${TARGET_DIR}"
cp -R "${SOURCE_DIR}" "${TARGET_DIR}"

echo "Installed Claude Code skill: ${SKILL_NAME}"
echo "Target: ${TARGET_DIR}"
