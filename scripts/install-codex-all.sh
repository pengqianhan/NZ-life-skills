#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
SKILLS_DIR="${REPO_DIR}/skills"

if [ ! -d "${SKILLS_DIR}" ]; then
  echo "No skills directory found at ${SKILLS_DIR}"
  exit 1
fi

for skill_dir in "${SKILLS_DIR}"/*; do
  [ -d "${skill_dir}" ] || continue
  bash "${SCRIPT_DIR}/install-codex-skill.sh" "$(basename "${skill_dir}")"
done

echo "Installed all Codex skills from ${SKILLS_DIR}"
