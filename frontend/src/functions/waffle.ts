import { RuntimeData } from "../hooks/api/runtimeData";

export type RuntimeDataWithWaffle = RuntimeData & {
  WAFFLE_FLAGS: RuntimeData["WAFFLE_FLAGS"];
};

export function flagIsActive(
  runtimeData: RuntimeData | undefined,
  flagName: string
): runtimeData is RuntimeDataWithWaffle {
  if (runtimeData?.WAFFLE_FLAGS) {
    for (const flag of runtimeData.WAFFLE_FLAGS) {
      if (flag[0] === flagName && flag[1] === true) {
        return true;
      }
    }
  }
  return false;
}